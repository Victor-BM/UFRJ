import random

class Eletrônicos:
    def __init__ (self, marca, modelo, tensao, preco):
        self.marca = marca
        self.modelo = modelo
        self.tensao = int(tensao)
        self.preco = float(preco)
        self.ligado = False

    def ligar_desligar (self):
        self.ligado = True if not self.ligado else False
    
    def verificar_estado (self):
        estado = 'ligado' if self.ligado else 'desligado'
        return estado
    
    def mostra_dados (self):
        print(f'\nDispositivo: {self.__class__.__name__.lower()}\nMarca: {self.marca}\nModelo: {self.modelo}')
        print(f'Tensão: {self.tensao}\nPreço: {self.preco}\nEstado: {self.verificar_estado()}')

class Televisão (Eletrônicos):
    def __init__ (self, marca, modelo, tensao, preco, polegadas):
        Eletrônicos.__init__(self, marca, modelo, tensao, preco)
        self.polegadas = int(polegadas)
        self.canal = 1
        self.volume = 1

    def mudar_canal(self, novo_canal):
        if self.ligado:
            if 1 <= novo_canal < 5000:
                self.canal = novo_canal
                print(f'Canal alterado para: {self.canal}')
            else:
                print('Canal inválido!')
        else:
            self.canal = 1
            print(f'A {self.__class__.__name__.lower()} está desligada! Ligue-a!')

    def mudar_volume (self, novo_volume):
        if self.ligado:
            if 1 <= novo_volume < 100:
                self.volume = novo_volume
                print(f'Volume alterado para: {self.volume}')
            else:
                print('Volume inválido!')
        else:
            self.volume = 1
            print(f'A {self.__class__.__name__.lower()} está desligada! Ligue-a!')    

class Rádio (Eletrônicos):
    def __init__ (self, marca, modelo, tensao, preco):
        Eletrônicos.__init__(self, marca, modelo, tensao, preco)
        self.frequencia = 87.5
        self.volume = 1
    
    def sintonizar (self):
        if self.ligado:
            self.frequencia = round(random.uniform(87.5, 108), 2)
            print(f'Frequência definida para {self.frequencia} MHz')
        else:
            print(f'O {self.__class__.__name__.lower()} está desligado! Ligue-o!')

    def mudar_volume (self, novo_volume):
        if self.ligado:
            if 1 <= novo_volume < 100:
                self.volume = novo_volume
                print(f'Volume alterado para: {self.volume}')
            else:
                print('Volume inválido!')
        else:
            self.volume = 1
            print(f'O {self.__class__.__name__.lower()} está desligado! Ligue-o!') 

Tv01 = Televisão('toshiba', 'seial', 227, 1050, 50)
radio01 = Rádio('marquinha', 'seial', 110, 34)
Tv01.ligar_desligar()
radio01.ligar_desligar()
radio01.sintonizar()
radio01.mudar_volume(392)
Tv01.mudar_canal(54)
Tv01.mudar_volume(45)
radio01.mostra_dados()
Tv01.ligar_desligar()
Tv01.mostra_dados()
