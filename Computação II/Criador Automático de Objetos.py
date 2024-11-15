import random

class Item:
    def __init__ (self, nome = '', tipo = '', disponibilidade = 0, descrição ='', estado = False):
        self.nome = nome
        self.tipo = tipo
        self.disponibilidade = int(disponibilidade)
        self.descrição = descrição
        self.estado = estado
    
    def exibir_informação (self):
        print(f'Nome: {self.nome}\nTipo: {self.tipo}\nDisponibilidade: {self.disponibilidade}\nDescrição: {self.descrição}')

lst = []
for i in range (100):
    lst.append('item' + str(i))
todos_items = {k: Item() for k in lst}

def gera_items():
    for element in dict.keys(todos_items):
        if todos_items[element].estado == False:
            todos_items[element].tipo = random.choice(['vida', 'sanidade'])
            todos_items[element].disponibilidade = random.randint(1, 20)
            todos_items[element].estado = True
            if todos_items[element].tipo == 'vida':
                #cura
                #element.nome
                #element.descrição
                a = 2
            else:
                #sanidade
                #element.nome
                #element.descrição
                a = 3
    for element in dict.values(todos_items):
        print(element)
gera_items()
