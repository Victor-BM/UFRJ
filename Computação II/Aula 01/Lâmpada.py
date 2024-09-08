import datetime
import time

class Lâmpada:
    def __init__(self):
        self.ligada = False
        self.cor = 'branca'
        self.intensidade = 1
    
    def ligar(self):
        if not self.ligada:
            self.ligada = True
            print('A lâmpada foi ligada')
        else:
            print('A lâmpada já está ligada')
    
    def desligar (self):
        if self.ligada:
            self.ligada = False
            print('A lâmpada foi desligada')
        else:
            print('A lâmpada já está desligada')

    def mudar_cor (self, nova_cor):
        cores = ['branca', 'vermelha', 'verde', 'azul']
        if nova_cor.lower() in cores and nova_cor != self.cor:
            self.cor = nova_cor
            print(f'Cor alterada para: {self.cor}')
        elif nova_cor.lower() in cores and nova_cor == self.cor:
            print(f'A cor permanece em: {self.cor}')
        else:
            print('Cor inválida!')
    
    def qual_estado (self):
        estado = 'Ligada' if self.ligada else 'Desligada'
        print(f'\nEstado: {estado}\nCor: {self.cor}\nIntensidade: {self.intensidade}\n')
    
    def aumentar_intensidade (self):
        if 1 <= self.intensidade <= 5:
            self.intensidade += 1
            print(f'Intensidade aumentada para: {self.intensidade}')
        else:
            print('A intensidade já está no máximo!')
    
    def diminuir_intensidade (self):
        if 1 <= self.intensidade <= 5:
            self.intensidade -= 1
            print(f'Intensidade diminuída para: {self.intensidade}')
        else:
            print('A intensidade já está no mínimo!')
    
    def configurar_timer (self, hora, estado, cor = 'branca', intensidade = 1):
        agora = datetime.datetime.now()
        horario_atual = agora.strftime('%H:%M')
        if hora == horario_atual:
            if estado.lower() == 'ligar':
                self.ligar()
            elif estado.lower() == 'desligar':
                self.desligar()
            else:
                return 'Estado Inválido'
            self.mudar_cor(cor)
            if 1 <= intensidade <= 5:
                self.intensidade = intensidade
            else:
                print('Intensidade não modificada')
            print('Configuração da lâmpada modificada')
        else:
            print('Configuração da lâmpada não modificada')

lampada01 = Lâmpada()
lampada01.configurar_timer('20:38', 'Ligar', 'Vermelha', 5)
lampada01.qual_estado()
time.sleep(30)
lampada01.configurar_timer('20:39', 'Ligar', 'Vermelha', 3)
lampada01.qual_estado()