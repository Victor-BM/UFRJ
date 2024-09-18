import random as rnd
    
class Eventos:
    def __init__ (self):
        pass

class Item:
    def __init__ (self, id, nome, tipo, disponibilidade, descrição):
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.disponibilidade = int(disponibilidade)
        self.descrição = descrição
    
    def exibir_informação (self):
        print(f'Nome: {self.nome}\nTipo: {self.tipo}\nDisponibilidade: {self.disponibilidade}\nDescrição: {self.descrição}')

class Inventário:
    def __init__ (self):
        self.items = []
        self.espaço = 15
    
    def adicionar_item (self, item):
        self.items.append(item)
        print('Item adicionado no inventário')
    
    def remover_item (self, item):
        if item in self.items:
            self.items.remove(item)
            print('Item removido do inventário')
        else:
            print('Item não presente no inventário')

    def listar_items (self):
        if not self.items:
            print('Inventário Vazio')
        else:
            for item in self.items:
                print(f'{item.exibir_informação()}')

class Entidades:
    def __init__ (self, fisicalidade, racionalidade, emocionalidade, vida, energia):
        self.fisicalidade = fisicalidade
        self.racionalidade = racionalidade
        self.emocionalidade = emocionalidade
        self.vida = vida
        self.energia = energia
    
    def rolar_D20 (self):
        resultado = rnd.randint(1, 20)
        return resultado

class Jogador (Entidades):
    def __init__(self, fisicalidade, racionalidade, emocionalidade, vida, energia, moral, sanidade, nome):
        Entidades.__init__(self, fisicalidade, racionalidade, emocionalidade, vida, energia)
        self.moral = moral
        self.sanidade = sanidade
        self.nome = nome

    def ficha (self):
        print(f'Fisicalidade: {self.fisicalidade}\nRacionalidade: {self.racionalidade}\nEmocionalidade: {self.emocionalidade}')
        print(f'Vida: {self.vida}\nEnergia: {self.energia}\nSanidade: {self.sanidade}\nMoral: {self.moral}')   

    def descansar (self):
        self.energia += 1
    
    def recuperar_vida (self, item):
        if item.tipo == 'vida':
            self.vida += item.disponibilidade
            inventario.remover_item(item)
    
    def recuperar_sanidade (self, item):
        if item.tipo == 'sanidade':
            self.sanidade += item.disponibilidade
            inventario.remover_item(item)
    
    def recuperar_moral (self, item):
        if item.tipo == 'moral':
            self.moral += item.disponibilidade
            inventario.remover_item(item)
    
    def combate_fisicalidade (self, inimigo):
        if self.fisicalidade < inimigo.fisicalidade:
            if self.rolar_D20() > 15 and inimigo.rolar_D20() < 5:
                dano = 0
            elif inimigo.rolar_D20() < 15:
                dano = -(inimigo.fisicalidade)
            else:
                dano = -(inimigo.fisicalidade) - 3
        elif self.fisicalidade == inimigo.fisicalidade:
            if self.rolar_D20() > 15 and inimigo.rolar_D20() < 5:
                dano = self.fisicalidade
            elif self.rolar_D20() < 5 and inimigo.rolar_D20() > 15:
                dano = -(inimigo.fisicalidade)
            else:
                dano = 0
        else:
            if self.rolar_D20() < 5 and inimigo.rolar_D20() > 15:
                dano = 0
            elif self.rolar_D20() < 15:
                dano = self.fisicalidade
            else:
                dano = self.fisicalidade + 3
        return dano
        
    def combate_racionalidade (self, inimigo):
        if self.racionalidade < inimigo.racionalidade:
            if self.rolar_D20() > 15 and inimigo.rolar_D20() < 5:
                dano = 0
            elif inimigo.rolar_D20() < 15:
                dano = -(inimigo.racionalidade)
            else:
                dano = -(inimigo.racionalidade) - 3
        elif self.racionalidade == inimigo.racionalidade:
            if self.rolar_D20() > 15 and inimigo.rolar_D20() < 5:
                dano = self.racionalidade
            elif self.rolar_D20() < 5 and inimigo.rolar_D20() > 15:
                dano = -(inimigo.racionalidade)
            else:
                dano = 0
        else:
            if self.rolar_D20() < 5 and inimigo.rolar_D20() > 15:
                dano = 0
            elif self.rolarD20() < 15:
                dano = self.racionalidade
            else:
                dano = self.racionalidade + 3
        return dano
    
    def combate_emocionalidade (self, inimigo):
        if self.emocionalidade < inimigo.emocionalidade:
            if self.rolar_D20() > 15 and inimigo.rolar_D20() < 5:
                dano = 0
            elif inimigo.rolar_D20() < 15:
                dano = -(inimigo.emocionalidade)
            else:
                dano = -(inimigo.emocionalidade) - 3
        elif self.emocionalidade == inimigo.emocionalidade:
            if self.rolar_D20() > 15 and inimigo.rolar_D20() < 5:
                dano = self.emocionalidade
            elif self.rolar_D20() < 5 and inimigo.rolar_D20() > 15:
                dano = -(inimigo.emocionalidade)
            else:
                dano = 0
        else:
            if self.rolar_D20() < 5 and inimigo.rolar_D20() > 15:
                dano = 0
            elif self.rolar_D20() < 15:
                dano = self.emocionalidade
            else:
                dano = self.emocionalidade + 3
        return dano

class Monstros (Entidades):
    pass

inventario = Inventário()
jogador = Jogador(4, 3, 2, 10, 5, 1, 1, 'ajjsjdjd')
jogador.descansar()
print(jogador.energia)
item01 = Item(4994, 'bandaid', 'vida', '3', 'recupera um pouquin de vida')
inventario.adicionar_item(item01)
inventario.listar_items()
jogador.recuperar_vida(item01)
print(jogador.vida)
inventario.listar_items()