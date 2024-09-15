class Veículo:
    def __init__ (self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = int(ano)
        self.movimento = False

    def partir(self):
        if self.movimento:
            self.movimento = False
            print(f'O {self.marca} {self.modelo} do ano {self.ano} não está em movimento')
        else:
            self.movimento = True
            print(f'O {self.marca} {self.modelo} do ano {self.ano} está em movimento')
            

class Motorizado (Veículo):
    def __init__(self, marca, modelo, ano, potência, combustível):
        Veículo	.__init__(self, marca, modelo, ano)
        self.potência = potência
        self.combustível = combustível
    
    def alterarCombustível (self, novoCombustível):
        print(f'Antigo combustível: {self.combustível}\nNovo combustível: {novoCombustível}')
        self.combustível = novoCombustível

class Elétrico (Veículo):
    def __init__(self, marca, modelo, ano, autonomia, tempo_de_recarga):
        Veículo.__init__(self, marca, modelo, ano)
        self.autonomia = float(autonomia)
        self.tempo_de_recarga = float(tempo_de_recarga)
    
    def alterarAutonomia (self, novaAutonomia):
        print(f'Antiga autonomia: {self.autonomia}\nNova autonomia: {novaAutonomia}')
        self.autonomia = novaAutonomia

class Híbrido (Motorizado, Elétrico):
    def __init__(self, marca, modelo, ano, potência, combustível, autonomia, tempo_de_recarga, capacidade_tanque, consumo_combustível):
        Motorizado.__init__(self, marca, modelo, ano, potência, combustível)
        Elétrico.__init__(self, marca, modelo, ano, autonomia, tempo_de_recarga)
        self.capacidade_tanque = float(capacidade_tanque)
        self.consumo_combustível = float(consumo_combustível)

carro_motorizado = Motorizado("Chevrolet", "Onix LT", 2022, "100cv", "Gasolina")
carro_motorizado.alterarCombustível("Etanol")
carro_motorizado.partir()
print('\n\n')

carro_eletrico = Elétrico("Tesla", "Model 3", 2020, 500, 30)
carro_eletrico.alterarAutonomia(600)
carro_eletrico.partir()
print('\n\n')

carro_hibrido = Híbrido("Toyota", "Prius", 2019, "100hp", "Gasolina", 200, 25, 40, 15)
carro_hibrido.partir()
carro_hibrido.alterarCombustível("Etanol")
carro_hibrido.alterarAutonomia(220)
print('\n\n')
