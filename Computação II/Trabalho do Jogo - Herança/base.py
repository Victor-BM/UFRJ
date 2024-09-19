import random
import docs
    
class Eventos:
    def __init__ (self):
        self.dia = 0

    def eventos_clima (self):
        clima = random.choice(['Chuva Ácida', 'Tempestade Radioativa', 'Inverno Nuclear', 'Inferno Solar', 'Ameno', 'Ascensão das Trevas'])
        if clima == 'Chuva Ácida':
            return (-5, None)
        elif clima == 'Tempestade Radioativa':
            return (-15, 'desconexão')
        elif clima == 'Inverno Nuclear':
            return (-20, 'perturbação')
        elif clima == 'Inferno Solar':
            return (-25, 'desconexão')
        elif clima == 'Ascensão das Trevas':
            return (0, 'quebra mental')
        return (0, None)
        #gerar o texto baseado no clima
    
    def eventos_sanidade (self):
        evento = random.choice(['Artefato Além da Compreensão', 'Ecos Imemoriais', 'Não Há Esperança', 'Essas vozes falam a verdade?'])
        if evento == 'Artefato Além da Compreensão':
            return 'ruptura de realidade'
        elif evento == 'Ecos Imemoriais':
            return 'desconexão'
        elif evento == 'Não Há Esperança':
            return 'perturbação'
        elif evento == 'Essas vozes falam a verdade?':
            return 'quebra mental'

class Item:
    def __init__ (self, nome, tipo, disponibilidade, descrição):
        self.nome = nome
        self.tipo = tipo
        self.disponibilidade = int(disponibilidade)
        self.descrição = descrição
    
    def exibir_informação (self):
        print(f'Nome: {self.nome}\nTipo: {self.tipo}\nDisponibilidade: {self.disponibilidade}\nDescrição: {self.descrição}')

class Inventário:
    def __init__ (self):
        self.items = []
        self.espaço = 5
    
    def adicionar_item (self, item):
        if len(self.items) == 5:
            print('Inventário Cheio!')
        else:
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
    def __init__ (self, fisicalidade, racionalidade, emocionalidade):
        self.fisicalidade = fisicalidade
        self.racionalidade = racionalidade
        self.emocionalidade = emocionalidade
        self.vida_máx = 100
        self.energia_máx = 100
        self.vida = self.vida_máx
        self.energia = self.energia_máx
        self.sorte = 20*[1]
        self.estado = True
        
    def rolar_D20 (self):
        numero = []
        for i in range(1, 21):
            numero.append(i)
        resultado = random.choices(numero, weights = self.sorte, k =1)
        return resultado[0]
        
    def se_machucar (self, dano):
        if dano < 0:
            self.vida -= dano
            if self.vida <= 0:
                self.estado = False
                
class Monstros (Entidades):
    def __init__(self, tipo, fisicalidade, racionalidade, emocionalidade):
        super().__init__(fisicalidade, racionalidade, emocionalidade)
    
    def debuff_vida (self):
        if 75 <= self.vida:
            self.sorte = 20*[1]
        elif 50 <= self.vida < 75:
            for i in range (1, 16):
                self.sorte[i] += 1
        elif 25 <= self.vida < 50:
            for i in range (1, 11):
                self.sorte[i] += 1
        elif 0 <= self.vida < 25:
            for i in range (1, 6):
                self.sorte[i] += 1
    
class Jogador (Entidades, Eventos):
    def __init__(self, fisicalidade, racionalidade, emocionalidade):
        Entidades.__init__(self, fisicalidade, racionalidade, emocionalidade)
        Eventos.__init__(self)
        self.sanidade_máx = 100
        self.sanidade = self.sanidade_máx

    def ficha (self):
        print(f'Fisicalidade: {self.fisicalidade}\nRacionalidade: {self.racionalidade}\nEmocionalidade: {self.emocionalidade}')
        print(f'Vida: {self.vida}\nEnergia: {self.energia}\nSanidade: {self.sanidade}')   
    
    def explorar (self):
        if self.energia >= 5:
            self.energia -= 5
        else:
            self.descansar(15)
            self.sanidade -= 10

    def descansar (self, horas_de_descanso):
        self.energia += (5*horas_de_descanso)
        if self.energia >= self.energia_máx:
            self.energia = self.energia_máx
        if horas_de_descanso >= 8:
            return self.eventos_clima()
        self.dia += 1

    def curar (self, item):
        if item.tipo == 'vida':
            self.vida += item.disponibilidade
            inventario.remover_item(item)
            if self.vida >= self.vida_máx:
                self.vida = self.vida_máx
    
    def recuperar_sanidade (self, item):
        if item.tipo == 'sanidade':
            self.sanidade += item.disponibilidade
            inventario.remover_item(item)
            if self.sanidade >= self.sanidade_máx:
                self.sanidade = self.sanidade_máx
    
    def perder_sanidade(self):
        trauma = self.eventos_sanidade()
        if trauma == 'desconexão':
            self.sanidade -= 25
        elif trauma == 'perturbação':
            self.sanidade -= 50
        elif trauma == 'quebra mental':
            self.sanidade -= 75
        elif trauma == 'ruptura de realidade':
            self.sanidade -= 100
    
    def debuff_sanidade (self):
        if 75 <= self.sanidade:
            self.sorte = 20*[1]
        elif 50 <= self.sanidade < 75:
            #mentiras
            for i in range (1, 16):
                self.sorte[i] += 1
        elif 25 <= self.sanidade < 50:
            for i in range (1, 11):
                self.sorte[i] += 1
        elif 0 <= self.sanidade < 25:
            for i in range (1, 6):
                self.sorte[i] += 1
        elif -25 <= self.sanidade < 0:
            for i in range (16, 21):
                self.sorte[i] = 0
        elif -50 <= self.sanidade < -25:
            for i in range (11, 16):
                self.sorte[i] = 0
        else:
            for i in range(6, 11):
                self.sorte[i] = 0

    def combater (self, inimigo, modalidade):
        dado_jogador = self.rolar_D20()
        dado_inimigo = inimigo.rolar_D20()
        if modalidade == 'fisicalidade':
            if self.fisicalidade < inimigo.fisicalidade:
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano = 0
                elif dado_inimigo < 15:
                    dano = -(inimigo.fisicalidade)
                else:
                    dano = -(inimigo.fisicalidade) - 3
            elif self.fisicalidade == inimigo.fisicalidade:
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano = self.fisicalidade
                elif dado_jogador < 5 and dado_inimigo > 15:
                    dano = -(inimigo.fisicalidade)
                else:
                    dano = 0
            else:
                if dado_jogador < 5 and dado_inimigo > 15:
                    dano = 0
                elif dado_jogador < 15:
                    dano = self.fisicalidade
                else:
                    dano = self.fisicalidade + 3
        elif modalidade == 'racionalidade':
            if self.racionalidade < inimigo.racionalidade:
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano = 0
                elif dado_inimigo < 15:
                    dano = -(inimigo.racionalidade)
                else:
                    dano = -(inimigo.racionalidade) - 3
            elif self.racionalidade == inimigo.racionalidade:
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano = self.racionalidade
                elif dado_jogador < 5 and dado_inimigo > 15:
                    dano = -(inimigo.racionalidade)
                else:
                    dano = 0
            else:
                if dado_jogador < 5 and dado_inimigo > 15:
                    dano = 0
                elif dado_jogador < 15:
                    dano = self.racionalidade
                else:
                    dano = self.racionalidade + 3
        elif modalidade == 'emocionalidade':
            if self.emocionalidade < inimigo.emocionalidade:
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano = 0
                elif dado_inimigo < 15:
                    dano = -(inimigo.emocionalidade)
                else:
                    dano = -(inimigo.emocionalidade) - 3
            elif self.emocionalidade == inimigo.emocionalidade:
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano = self.emocionalidade
                elif dado_jogador < 5 and dado_inimigo > 15:
                    dano = -(inimigo.emocionalidade)
                else:
                    dano = 0
            else:
                if dado_jogador < 5 and dado_inimigo > 15:
                    dano = 0
                elif dado_jogador < 15:
                    dano = self.emocionalidade
                else:
                    dano = self.emocionalidade + 3
        return dano
    #add frases e interações com as personalidades

    def fugir (self):
        self.energia -= 10
        return True if self.energia >= 50 else False
