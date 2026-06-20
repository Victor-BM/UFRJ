import time
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class EnsaioTracao:

    def __init__(self, filepath: str, largura: float, espessura: float, l0: float):
        '''Condições do corpo de prova
        filepath -> caminho do arquivo Excel
        largura, espessura e l0 (comprimento inicial) em milímetros
        '''
        self.filepath = filepath
        self.area_nominal = largura * espessura  #Área inicial A0 (mm²)
        self.l0 = l0  #Comprimento inicial (mm)

        self.df = None
        self.modulo_elastico = None
        self.limite_escoamento = None
        self.lrt = None
        self.ruptura = None

        self._carregar_e_processar_dados()

    def _carregar_e_processar_dados(self):
        self.df = pd.read_excel(self.filepath)
        self.df.columns = self.df.columns.str.strip() #remove espaços/caracteres especiais
        self.df['Tensao'] = (self.df['Carga [N]']/self.area_nominal) #Tensão de Engenharia [MPa]
        self.df['Deformacao'] = (self.df['Deslocamento [mm]']/self.l0) 


    def calcular_propriedades(self, lim_inf_regiao_elastica=0.005, lim_sup_regiao_elastica=0.02): #Valores default para PVDF, mas tem que ir mudando no olho mesmo vendo se bate a reta gerada com os pontos fornecidos
        self.lrt = self.df['Tensao'].max()

        #Limita os dados analisados para a Região Elástica para calcular E (lim_inf = 0.005 para ignorar valores iniciais que estão mais sujeitos a ruídos)
        regiao_elastica = self.df[(self.df['Deformacao'] >= lim_inf_regiao_elastica) & (self.df['Deformacao'] <= lim_sup_regiao_elastica)]
        if regiao_elastica.empty:
            raise ValueError('Região elástica vazia. Ajuste os limites de deformação')
        #Regressão Linear Tensao = E * Deformacao + b
        E, b = np.polyfit(regiao_elastica['Deformacao'], regiao_elastica['Tensao'], 1)
        self.modulo_elastico = E
        self.b_elastico = b

        #Limite de Escoamento (Reta Paralela ao Elástico partindo de Deformacao = 0.002)
        self.df['Tensao_Offset'] = self.modulo_elastico*(self.df['Deformacao'] - 0.002) + self.b_elastico
        #Encontrar a interseção aproximada onde a curva do ensaio cruza a linha de offset (onde a diferença muda de sinal)
        self.df['Diferenca'] = self.df['Tensao'] - self.df['Tensao_Offset']
        df_busca = self.df[self.df['Deformacao'] > 0.002]
        idx_escoamento = (df_busca['Diferenca'] < 0).idxmax()
        self.limite_escoamento = self.df.loc[idx_escoamento, 'Tensao']

        idx_ruptura = self.df.index[-1]
        self.ruptura = self.df.loc[idx_ruptura, 'Tensao']

        print('--- PROPRIEDADES MECÂNICAS CALCULADAS ---')
        print(f'Módulo de Elasticidade (E): {self.modulo_elastico:.2f} MPa')
        print(f'Limite de Escoamento (\u03c3_e): {self.limite_escoamento:.2f} MPa')
        print(f'Limite de Resistência à Tração (LRT): {self.lrt:.2f} MPa')
        print(f'Ruptura: {self.ruptura:.2f} MPa')
        print("-----------------------------------------")

    def plotar_grafico_estatico(self):
        plt.figure(figsize=(10, 6))
        plt.plot(self.df['Deformacao'],
            self.df['Tensao'],
            label='Curva do Ensaio',
            color='blue')
        

        resposta = str(input('Deseja plotar a Linha de Offset? [S] ou [N] ')).lower()
        if resposta == 's':
            df_offset_plot = self.df[self.df['Deformacao'] <= self.df['Deformacao'].max() * 0.2]
            plt.plot(
                df_offset_plot['Deformacao'],
                self.modulo_elastico * (df_offset_plot['Deformacao'] - 0.002) + self.b_elastico, 
                '--',
                color='orange',
                label='Offset 0.2%')

        #Ponto do Escoamento
        idx_escoamento = self.df[self.df['Tensao'] == self.limite_escoamento].index
        plt.scatter(
            self.df.loc[idx_escoamento, 'Deformacao'],
            self.limite_escoamento,
            color='red',
            zorder=5,
            label=f'Escoamento: {self.limite_escoamento:.2f} MPa')

        #Ponto de LRT
        idx_lrt = self.df['Tensao'].idxmax()
        plt.scatter(
            self.df.loc[idx_lrt, 'Deformacao'],
            self.lrt,
            color='green',
            zorder=5,
            label=f'LRT: {self.lrt:.2f} MPa')
        
        #Ponto de Ruptura
        idx_ruptura = self.df[self.df['Tensao'] == self.ruptura].index
        plt.scatter(
            self.df.loc[idx_ruptura, 'Deformacao'],
            self.ruptura,
            color='pink',
            zorder=5,
            label=f'Ruptura: {self.ruptura:.2f} MPa')

        plt.title('Gráfico Tensão de Engenharia x Deformação')
        plt.xlabel('Deformação de Engenharia $\epsilon$ [mm/mm]')
        plt.ylabel('Tensão de Engenharia $\sigma$ [MPa]')
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.show()

class SimuladorEnsaio:

    def __init__(self, ensaio: EnsaioTracao):
        '''Simula o ensaio em tempo real (de maneira acelerada) e recebe um objeto da classe EnsaioTracao'''
        self.ensaio = ensaio

    def simular(self, passo_frames: int = 1, intervalo_ms: int = 12):
        '''Plota a animação do ensaio de tração simulando o tempo real
        passo_frames -> de quantos em quantos pontos do dataset o gráfico avança por frame
        intervalo_ms -> tempo de atualização do frame em milissegundos
        '''
        fig, ax = plt.subplots(figsize=(10, 6))
        (linha,) = ax.plot([], [], color='blue', lw=2, label='Progresso do Ensaio')

        #Configurações de limite dinâmicas baseadas nos dados reais
        ax.set_xlim(0, self.ensaio.df['Deformacao'].max() * 1.05)
        ax.set_ylim(
            self.ensaio.df['Tensao'].min(),
            self.ensaio.df['Tensao'].max() * 1.1,
        )

        ax.set_title('Simulação em Tempo Real: Ensaio de Tração')
        ax.set_xlabel('Deformação de Engenharia $\epsilon$ [mm/mm]')
        ax.set_ylabel('Tensão de Engenharia $\sigma$ [MPa]')
        ax.grid(True, linestyle='--', alpha=0.5)
        ax.legend(loc='upper left')

        # Dados para animação
        x_data = self.ensaio.df['Deformacao'].values
        y_data = self.ensaio.df['Tensao'].values
        total_pontos = len(x_data)

        def init():
            linha.set_data([], [])
            return (linha,)

        def update(frame):
            atual = frame * passo_frames
            #Se o cálculo passar do total ou for o último frame da lista, força o gráfico a desenhar até a última linha real do Excel
            if atual >= total_pontos - 1 or frame == (total_pontos // passo_frames):
                atual = total_pontos - 1

            x_atual = x_data[: atual + 1]
            y_atual = y_data[: atual + 1]
            
            linha.set_data(x_atual, y_atual)

            #Zoom Out
            if atual > 1:
                max_x_momento = x_atual.max()
                max_y_momento = y_atual.max()
                min_y_momento = y_atual.min()

                #Define limites mínimos para o início do ensaio não ficar colado nas bordas
                limite_x = max(max_x_momento * 1.1, 0.005)
                limite_y_superior = max(max_y_momento * 1.1, 5.0)
                limite_y_inferior = min(min_y_momento - 1, -0.5)

                #Atualiza os limites do gráfico à medida que o ensaio cresce
                ax.set_xlim(-0.0002, limite_x)
                ax.set_ylim(limite_y_inferior, limite_y_superior)

            #Para a animação no último ponto
            if atual == total_pontos - 1:
                ani.event_source.stop()

            return (linha,)

        ani = FuncAnimation(
            fig,
            update,
            frames=range(0, (total_pontos // passo_frames) + 2),
            init_func=init,
            blit=False, 
            interval=intervalo_ms,
            repeat=False,)

        plt.show()

def pvdf_T1 ():
    ensaio_pvdf_T1 = EnsaioTracao("PCM PVDF prof Pedro t 1.xlsx", 14, 4, 70)
    simulador_pvdf_T1 = SimuladorEnsaio(ensaio_pvdf_T1)

    ensaio_pvdf_T1.calcular_propriedades(lim_inf_regiao_elastica=0.005, lim_sup_regiao_elastica=0.012)
    ensaio_pvdf_T1.plotar_grafico_estatico()
    simulador_pvdf_T1.simular()

def pvdf_T2 ():
    ensaio_pvdf_T2 = EnsaioTracao("PCM PVDF prof Pedro t 2.xlsx", 14, 4, 70)
    simulador_pvdf_T2 = SimuladorEnsaio(ensaio_pvdf_T2)

    ensaio_pvdf_T2.calcular_propriedades(lim_inf_regiao_elastica=0.005, lim_sup_regiao_elastica=0.012)
    ensaio_pvdf_T2.plotar_grafico_estatico()
    simulador_pvdf_T2.simular()

def aluminio_T1 ():
    ensaio_aluminio_T1 = EnsaioTracao("PCM aluminio prof Pedro t 1.xlsx", 6, 1, 25)
    simulador_aluminio_T1 = SimuladorEnsaio(ensaio_aluminio_T1)

    ensaio_aluminio_T1.calcular_propriedades(lim_inf_regiao_elastica=0.01, lim_sup_regiao_elastica=0.032)
    ensaio_aluminio_T1.plotar_grafico_estatico()
    simulador_aluminio_T1.simular()

def aluminio_T2 ():
    ensaio_aluminio_T2 = EnsaioTracao("PCM aluminio prof Pedro t 2.xlsx", 6, 1, 25)
    simulador_aluminio_T2 = SimuladorEnsaio(ensaio_aluminio_T2)

    ensaio_aluminio_T2.calcular_propriedades(lim_inf_regiao_elastica=0.01, lim_sup_regiao_elastica=0.032)
    ensaio_aluminio_T2.plotar_grafico_estatico()
    simulador_aluminio_T2.simular()

def main():
    aluminio_T1()
    aluminio_T2()
main()