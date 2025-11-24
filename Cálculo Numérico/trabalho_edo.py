'''
Trabalho EDO - Cálculo Numérico

Prof: Maria Helena

Aluno: Gabriel Peixoto Costa Marques Barbosa          DRE: 124026590
Aluno: Felipe Mariano Lessa Chaves                    DRE: 124055298
Aluno: Víctor Bernardes de Morais                     DRE: 124031375

Feito no VSCode com Python 3.11.3
'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import abc

#EDO: dC/dt = -0.06 * C

class ProblemaPoluicao:
    '''Representa a solução analítica da EDO
    C(t) =  10^7 * e^(-0.06t)
    '''
    def __init__ (self, c_o = 1e7, k = 0.06):
        self.c_o = c_o
        self.k = k
    
    def resolver_exato (self, t):
        return self.c_o * np.exp(-self.k*t)

class Solucionador (abc.ABC):
    def __init__ (self, nome):
        self.exata = ProblemaPoluicao()
        self.nome = nome
    
    def derivada (self, t, c):
        return -0.06*c

    @abc.abstractmethod
    def resolver (self, h, t_final):
       pass

    def grafico (self, h, t_final):
        t_num, c_num = self.resolver(h, t_final)

        t_exata = np.linspace(0, t_final, 200)
        c_exata = self.exata.resolver_exato(t_exata)

        plt.figure(figsize = (8,5))
        plt.plot(t_exata, c_exata, 'k-', linewidth = 2, label = 'Solução Exata')
        plt.plot(t_num, c_num, 'r--o', label = f'{self.nome} (h = {h})')
        plt.title('Comparação Gráfica')
        plt.xlabel('Tempo (semanas)')
        plt.ylabel('Concentração do Poluente partes/m³')
        plt.legend()
        plt.grid(True, linestyle = ':', alpha = 0.6)
        plt.show()

    def relatorio (self, lista_h, t_obj):
        resultados = []
        c_exata = self.exata.resolver_exato(t_obj)

        for h in lista_h:
            t_num, c_num = self.resolver(h, t_obj) #t_num será ignorado
            c_obj = c_num[-1]
            erro_abs = abs(c_obj - c_exata)
            erro_rel = (erro_abs/c_exata)*100

            resultados.append({
                'Passo (h)' : h, 
                'Valor C - Numérico' : c_obj,
                'Valor C - Exato' : c_exata,
                'Erro Absoluto' : erro_abs,
                'Erro Relativo (%)' : erro_rel,
                })
        df = pd.DataFrame(resultados)
        print(df.to_string(index=False, float_format=lambda x: "{:.6f}".format(x)))

class Euler (Solucionador):
    def __init__ (self):
        Solucionador.__init__ (self, 'Euler')
    
    def resolver (self, h, t_final):
        t_values = np.arange(0, t_final + h/1000, h)
        c_values = np.zeros(len(t_values))
        c_values [0] = self.exata.c_o

        f = self.derivada

        for i in range (len(t_values) - 1):
            t, c = t_values[i], c_values[i]

            c_values[i+1] = c + (h*f(t, c))
        return t_values, c_values

class EulerModificado (Solucionador):
    def __init__ (self):
        Solucionador.__init__ (self, 'Euler Modificado')
    
    def resolver (self, h, t_final):
        t_values = np.arange(0, t_final + h/1000, h)
        c_values = np.zeros(len(t_values))
        c_values [0] = self.exata.c_o

        f = self.derivada

        for i in range (len(t_values) - 1):
            t, c = t_values[i], c_values[i]

            k1 = f(t, c)
            c_pred = c + (h*k1)
            k2 = f(t+h, c_pred)

            c_values[i+1] = c + (h/2)*(k1 + k2)

        return t_values, c_values

class RungeKutta (Solucionador):
    def __init__ (self):
        Solucionador.__init__ (self, 'Runge-Kutta 4ª')
    
    def resolver (self, h, t_final):
        t_values = np.arange(0, t_final + h/1000, h)
        c_values = np.zeros(len(t_values))
        c_values [0] = self.exata.c_o

        f = self.derivada

        for i in range (len(t_values) - 1):
            t, c = t_values[i], c_values[i]

            k1 = f(t, c)
            k2 = f(t+(h/2), c + h*(k1/2))
            k3 = f(t + (h/2), c + h*(k2/2))
            k4 = f(t + h, c + (h*k3))

            c_values[i+1] = c + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

        return t_values, c_values

def main():
    exato = ProblemaPoluicao()
    euler = Euler()
    euler_modificado = EulerModificado()
    rk4 = RungeKutta()
    lista_h = [7, 3.5, 1.75, 0.875, 0.4375]

    #1 - Para h = 3,5 semanas, determinar a concentração
    print(f'Solução Exata: {exato.resolver_exato(7)}')
    print(f'Método de Euler: {euler.resolver(3.5, 7)[1][-1]}')
    print(f'Método de Euler Modificado: {euler_modificado.resolver(3.5, 7)[1][-1]}')
    print(f'Método de Runge-Kutta de 4ª Ordem: {rk4.resolver(3.5, 7)[1][-1]}\n\n\n')

    #2 - Gráficos Comparativos para h = 3,5 semanas
    euler.grafico(3.5, 7)
    euler_modificado.grafico(3.5, 7)
    rk4.grafico(3.5, 7)

    #3 - Relatórios
    euler.relatorio(lista_h, 7)
    print('\n\n\n')
    euler_modificado.relatorio(lista_h, 7)
    print('\n\n\n')
    rk4.relatorio(lista_h, 7)
    print('\n\n\n')
main()