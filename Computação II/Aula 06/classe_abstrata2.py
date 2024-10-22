import abc

class Veículo (abc.ABC):
    def __init__(self, modelo, velocidade):
        self.modelo = modelo
        self._velocidade = velocidade

    @property
    def velocidade (self):
        return self._velocidade
    
    @velocidade.setter
    def velocidade (self, valor):
        if valor <= (self.velocidade*1.1):
            self._velocidade = valor
    
    @abc.abstractmethod
    def dirigir (self):
        pass

    def __str__ (self):
        return f'Modelo: {self.modelo}, Velocidade Máxima: {self.velocidade}km/h'
    
class CarroAutonomo (Veículo):
    def __init__ (self, modelo, velocidade, nível_autonomia):
        Veículo.__init__(self, modelo, velocidade)
        self.nível_autonomia = nível_autonomia
    
    def dirigir(self):
        return f'O carro autônomo {self.modelo} está operando no nível de autonomia {self.nível_autonomia}'
    
    def ativar_piloto_automatico (self):
        if self.nível_autonomia >= 3:
            return f'Piloto automático ativado para {self.modelo}, nível de autonomia {self.nível_autonomia}'
        return f'Piloto automático não disponiível para {self.modelo} com nível de autonomia {self.nível_autonomia}'
    
    def __str__ (self):
        return f'\nCarro autônomo\nModelo: {self.modelo}, Velocidade máxima: {self.velocidade}km/h, nível de autonomia: {self.nível_autonomia}\n'
    
class CaminhaoAutonomo (CarroAutonomo):
    def __init__(self, modelo, velocidade, nível_autonomia):
        super().__init__(modelo, velocidade, nível_autonomia)
    
    def dirigir(self):
        return f'O caminhão autônomo {self.modelo} está operando no nível de autonomia {self.nível_autonomia}'
    
    def __str__ (self):
        return f'\nCaminhão autônomo\nModelo: {self.modelo}, Velocidade máxima: {self.velocidade}km/h, nível de autonomia: {self.nível_autonomia}\n'
    
carro = CarroAutonomo("Tesla Model S", 200, 5)
print(carro)
carro.velocidade = 220
print(f"Nova velocidade: {carro.velocidade} km/h")
carro.velocidade = 210
print(f"Nova velocidade: {carro.velocidade} km/h")
print(carro.ativar_piloto_automatico())
carro_nivel_baixo = CarroAutonomo("Ford Focus", 180, 2)
print(carro_nivel_baixo.ativar_piloto_automatico())
caminhao = CaminhaoAutonomo("Volvo FH", 120, 4)
print(caminhao)
print(caminhao.dirigir())
