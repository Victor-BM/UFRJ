import random as rnd

class Periquito:
    def __init__(self, idade, cor, sexo, habitat):
        if sexo.lower() not in ['macho','fêmea']:
            print('Sexo inválido')
            return
        if habitat.lower() not in ['confinado', 'natureza']:
            print ('Habitat Inválido')
            return
        self.idade = float(idade)
        self.cor = cor
        self.sexo = sexo
        self.habitat = habitat
        self.estado = 'Pousado'

    def qual_estado(self, sexo, estado):
        possibilidades = ['Voando', 'Pousado', 'Botando Ovo']
        if sexo.lower() == 'macho':
            possibilidades.remove('Botando Ovo')
        escolha = rnd.choice(possibilidades)
        if estado != 'Voando':
            self.estado = escolha
        return self.estado 
    
    def ficha(self):
        return f'Idade: {self.idade}\nCor: {self.cor}\nSexo: {self.sexo}\nHabitat: {self.habitat}\nEstado: {self.qual_estado(self.sexo, self.estado)}'


class Canário:
    def __init__(self, idade, cor, sexo, habitat):
        if sexo.lower() not in ['macho','fêmea']:
            print('Sexo inválido')
            return
        if habitat.lower() not in ['confinado', 'natureza']:
            print ('Habitat Inválido')
            return
        self.idade = float(idade)
        self.cor = cor
        self.sexo = sexo
        self.habitat = habitat
        self.estado = 'Pousado'
        self.canto = self.cantar(self.habitat)

    def qual_estado(self, sexo, estado, canto):
        possibilidades = ['Voando', 'Pousado', 'Botando Ovo']
        if canto == 'Canta':
            possibilidades.append('Cantando') 
        if sexo.lower() == 'macho':
            possibilidades.remove('Botando Ovo')
        escolha = rnd.choice(possibilidades)
        if estado != 'Voando':
            self.estado = escolha
        return self.estado 
    
    def cantar (self, habitat):
        if habitat == 'natureza':
            return 'Canta'
        else:
            return rnd.choice(['Canta', 'Não Canta'])
    
    def ficha(self):
        return f'Idade: {self.idade}\nCor: {self.cor}\nSexo: {self.sexo}\nHabitat: {self.habitat}\nCanto: {self.canto}\nEstado: {self.qual_estado(self.sexo, self.estado, self.canto)}'
    
#Exemplos    
passaro01 = Periquito(23, 'Branco', 'Fêmea', 'Natureza')
print(passaro01.ficha())
passaro02 = Canário(45, 'Amarelo', 'Fêmea', 'Confinado')
print('\n\n\n')
print(passaro02.ficha())
print(passaro02.estado)
passaro03 = Canário(45, 'Amarelo', 'Fêmea', 'Gaiola')
print('\n\n\n')
#VAI DAR ERRO
print(passaro03.ficha())