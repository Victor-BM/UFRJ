class Leão:
    def __init__(self, idade, sexo, cor):
        self.idade = float(idade)
        self.sexo = sexo
        self.cor = cor
        self.comportamento = self.cacar(self.sexo)
    
    def cacar(self, sexo):
        if sexo.lower()  == 'fêmea':
            return 'Caça'
        elif sexo.lower() == 'macho':
            return 'Fica atoa'
        else:
            return 'Indefinido'
        
    def dormir (self, idade):
        if idade <= 1:
            return 'Dorme pouco'
        elif idade <= 5:
            return 'Não dorme'
        elif idade <= 8:
            return 'Dorme bastante'
        else:
            return 'Dorme sempre'
    
    def exibir_informacao(self):
        return f'Leão\nIdade: {self.idade}\nSexo: {self.sexo}\nCor: {self.cor}\nComportamento: {self.comportamento}\nSono: {self.dormir(self.idade)}\n\n'
    
        

class  Gato:
    def __init__(self, idade, sexo, cor):
        self.idade = float(idade)
        self.sexo = sexo
        self.cor = cor
        self.comportamento = self.qual_personalidade(self.cor)
    
    def qual_personalidade(self, cor):
        if cor.lower() == 'laranja':
            return 'Totalmente caótico'
        elif cor.lower() == 'branco':
            return 'Meio caótico'
        elif cor.lower() == 'preto':
            return 'Pouco caótico'
        elif cor.lower() == 'malhado':
            return 'Nada caótico'
        else:
            return 'Depende do dia'
        
    def dormir (self, idade):
        if idade <= 1:
            return 'Dorme pouco'
        elif idade <= 5:
            return 'Não dorme'
        elif idade <= 8:
            return 'Dorme bastante'
        else:
            return 'Dorme sempre'
    
    def exibir_informacao(self):
        return f'Gato\nIdade: {self.idade}\nSexo: {self.sexo}\nCor: {self.cor}\nComportamento: {self.comportamento}\nSono: {self.dormir(self.idade)}\n\n'
    

gato01 = Gato('0.5', 'macho', 'laranja')
gato02 = Gato('5', 'fêmea', 'preto')
gato03 = Gato('9', 'fêmea', 'cinza')
leao01 = Leão('0.5', 'macho', 'laranja')
leao02 = Leão('5', 'fêmea', 'albino')
leao03 = Leão('9', 'fêmea', 'laranja')
print(Gato.exibir_informacao(gato01))
print(Gato.exibir_informacao(gato02))
print(Gato.exibir_informacao(gato03))
print(Leão.exibir_informacao(leao01))
print(Leão.exibir_informacao(leao02))
print(Leão.exibir_informacao(leao03))
