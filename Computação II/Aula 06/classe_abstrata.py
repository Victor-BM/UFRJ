import abc

class Veiculo (abc.ABC):
    def __init__ (self, velocidade):
        self.__velocidade = velocidade
    
    @property
    def velocidade (self):
        return self.__velocidade
    
    @velocidade.setter
    def velocidade (self, valor):
        if valor >= 0:
            self.__velocidade = valor
    
    def exibir_velocidade (self):
        print(f'{self.__class__.__name__} está a {self.velocidade}km/h')
    
    @abc.abstractmethod
    def acelerar (self):
        pass

    @abc.abstractmethod
    def desacelerar (self):
        pass

class Moto (Veiculo):
    def __init__ (self, velocidade):
        Veiculo.__init__(self, velocidade)
    
    def acelerar(self):
        self.velocidade += 15
    
    def desacelerar(self):
        self.velocidade -= 10
        self.velocidade = max(0, self.velocidade)

class Carro (Veiculo):
    def __init__ (self, velocidade):
        Veiculo.__init__(self, velocidade)
    
    def acelerar(self):
        self.velocidade += 10
    
    def desacelerar(self):
        self.velocidade -= 8
        self.velocidade = max(0, self.velocidade)

class Caminhão (Veiculo):
    def __init__ (self, velocidade):
        Veiculo.__init__(self, velocidade)
    
    def acelerar(self):
        self.velocidade += 5
    
    def desacelerar(self):
        self.velocidade -= 3
        self.velocidade = max(0, self.velocidade)

carro01 = Carro(50)
caminh01 = Caminhão(30)
moto01 = Moto(80)

print(moto01.velocidade)
moto01.acelerar()
moto01.exibir_velocidade()
moto01.velocidade = 20
moto01.exibir_velocidade()
moto01.desacelerar()
moto01.desacelerar()
moto01.exibir_velocidade()
print('\n-------\n')
carro01.exibir_velocidade()
carro01.acelerar()
carro01.exibir_velocidade()
carro01.desacelerar()
carro01.exibir_velocidade()
print('\n-------\n')
caminh01.exibir_velocidade()
caminh01.acelerar()
caminh01.exibir_velocidade()
caminh01.desacelerar()
caminh01.exibir_velocidade()
