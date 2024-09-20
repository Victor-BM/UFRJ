import random
    
class Eventos:
    def __init__ (self):
        self.dia = 1

    def eventos_clima (self):
        clima = random.choice(['Chuva Ácida', 'Tempestade Radioativa', 'Inverno Nuclear', 'Inferno Solar', 'Ameno', 'Ascensão das Trevas'])
        if clima == 'Chuva Ácida':
            print('Chuva Ácida\nEba, chuva! Calma lá, chuva não derrete estátua, derrete?')
            return (-5, '')
        elif clima == 'Tempestade Radioativa':
            print('Tempestade Radioativa\nTempestade sempre causam terror, mas com relâmpagos radioativos eu acho que esse evento se torna um cadin mais de medo')
            return (-15, 'desconexão')
        elif clima == 'Inverno Nuclear':
            print('Inverno Nuclear\nTão frio tal qual Curitiba')
            return (-20, 'perturbação')
        elif clima == 'Inferno Solar':
            print('Inferno Solar\nTem certeza que o não tem pedaços do Sol caindo do céu? Como é possível um calor desses?')
            return (-25, 'desconexão')
        elif clima == 'Ascensão das Trevas':
            print('Ascensão das Trevas\nNão há mais estrelas no céu, o único brilho ao seu redor são dos demônios que te cercam!')
            return (0, 'quebra mental')
        return (0, '')
    
    def eventos_sanidade (self):
        evento = random.choice(['Artefato Além da Compreensão', 'Ecos Imemoriais', 'Não Há Esperança', 'Essas vozes falam a verdade?'])
        if evento == 'Artefato Além da Compreensão':
            print('Artefato Além da Compreensão\nVocê encontra ALGO que sua mente não é capaz de processar\ngshbfjdklvdvfkljfnkglgfdsg\nidjsfkldfaçkljgdfhafaks\ndjhkldjaksasdjlfhjfdadj')
            return 'ruptura de realidade'
        elif evento == 'Ecos Imemoriais':
            print('Ecos Imemoriais\nAs vozes das pessoas que frequentaram esse lugar pipocam em sua mente')
            return 'desconexão'
        elif evento == 'Não Há Esperança':
            print('Não Há Esperança\nToda a libertação almejada pelos oprimidos já não é mais possível, esse é, DE FATO, o fim da história\nSe você tivesse percebido seu lugar de classe antes, tudo poderia ser diferente...')
            return 'perturbação'
        elif evento == 'Essas vozes falam a verdade?':
            print('Essas vozes falam a verdade?\nComo confiar em desconhecidos?\nAinda mais se esses desconhecidos são fragmentos da minha própria mente?')
            return 'quebra mental'

class Item:
    def __init__ (self, nome = '', tipo = '', disponibilidade = 0, descrição =''):
        self.nome = nome
        self.tipo = tipo
        self.disponibilidade = int(disponibilidade)
        self.descrição = descrição
    
    def exibir_informação (self):
        print(f'Nome: {self.nome}\nTipo: {self.tipo}\nDisponibilidade: {self.disponibilidade}\nDescrição: {self.descrição}\n')

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
        if dano < 0 and isinstance(dano, int):
            self.vida += dano
            if self.vida <= 0:
                self.estado = False
                
class Monstros (Entidades):
    def __init__(self, espécie = '', fisicalidade = 0, racionalidade = 0, emocionalidade = 0):
        super().__init__(fisicalidade, racionalidade, emocionalidade)
        self.espécie = espécie
    
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
        if self.energia >= 10:
            self.energia -= 10
        else:
            self.descansar(8)
            self.sanidade -= 10

    def descansar (self, horas_de_descanso):
        dano_fisico, dano_mental = 0, ''
        if self.energia <= 50:
            self.energia += (5*horas_de_descanso)
            if self.energia >= self.energia_máx:
                self.energia = self.energia_máx
            if horas_de_descanso >= 8:
                dano_fisico, dano_mental = self.eventos_clima()
            self.dia += 1
        else:
            print('Você não está cansado o suficiente')
        return dano_fisico, dano_mental

    def curar (self, item):
        if item.tipo == 'vida':
            self.vida += item.disponibilidade
            if self.vida >= self.vida_máx:
                self.vida = self.vida_máx
            inventario.remover_item(item)
    
    def recuperar_sanidade (self, item):
        if item.tipo == 'sanidade':
            self.sanidade += item.disponibilidade
            if self.sanidade >= self.sanidade_máx:
                self.sanidade = self.sanidade_máx
            inventario.remover_item(item)
    
    def perder_sanidade(self, trauma_clima = 'vazio'):
        trauma_ev = 'vazio'
        if trauma_clima == 'vazio':
            trauma_ev = self.eventos_sanidade()
        if trauma_ev == 'desconexão' or trauma_clima == 'desconexão':
            self.sanidade -= 25
        elif trauma_ev == 'perturbação' or trauma_clima == 'perturbação':
            self.sanidade -= 50
        elif trauma_ev == 'quebra mental' or trauma_clima == 'quebra mental':
            self.sanidade -= 75
        elif trauma_ev == 'ruptura de realidade' or trauma_clima == 'ruptura de realidade':
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
                dano_inimigo = 0
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano_jogador = 0
                elif dado_inimigo < 15:
                    dano_jogador = -(inimigo.fisicalidade)
                else:
                    dano_jogador = -(inimigo.fisicalidade + 3)
            elif self.fisicalidade == inimigo.fisicalidade:
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano_jogador = self.fisicalidade
                    dano_inimigo = -dano_jogador
                elif dado_jogador < 5 and dado_inimigo > 15:
                    dano_inimigo = inimigo.fisicalidade
                    dano_jogador = -dano_inimigo
                else:
                    dano_jogador, dano_inimigo = 0, 0
            else:
                dano_jogador = 0
                if dado_jogador < 5 and dado_inimigo > 15:
                    dano_inimigo = 0
                elif dado_jogador < 15:
                    dano_inimigo = -(self.fisicalidade)
                else:
                    dano_inimigo = -(self.fisicalidade + 3)
        elif modalidade == 'racionalidade':
            if self.racionalidade < inimigo.racionalidade:
                dano_inimigo = 0
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano_jogador = 0
                elif dado_inimigo < 15:
                    dano_jogador = -(inimigo.racionalidade)
                else:
                    dano_jogador = -(inimigo.racionalidade + 3)
            elif self.racionalidade == inimigo.racionalidade:
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano_jogador = self.racionalidade
                    dano_inimigo = -dano_jogador
                elif dado_jogador < 5 and dado_inimigo > 15:
                    dano_inimigo = inimigo.racionalidade
                    dano_jogador = -dano_inimigo
                else:
                    dano_jogador, dano_inimigo = 0, 0
            else:
                dano_jogador = 0
                if dado_jogador < 5 and dado_inimigo > 15:
                    dano_inimigo = 0
                elif dado_jogador < 15:
                    dano_inimigo = -(self.racionalidade)
                else:
                    dano_inimigo = -(self.racionalidade + 3)
        elif modalidade == 'emocionalidade':
            if self.emocionalidade < inimigo.emocionalidade:
                dano_inimigo = 0
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano_jogador = 0
                elif dado_inimigo < 15:
                    dano_jogador = -(inimigo.emocionalidade)
                else:
                    dano_jogador = -(inimigo.emocionalidade + 3)
            elif self.emocionalidade == inimigo.emocionalidade:
                if dado_jogador > 15 and dado_inimigo < 5:
                    dano_jogador = self.emocionalidade
                    dano_inimigo = -dano_jogador
                elif dado_jogador < 5 and dado_inimigo > 15:
                    dano_inimigo = inimigo.emocionalidade
                    dano_jogador = -dano_inimigo
                else:
                    dano_jogador, dano_inimigo = 0, 0
            else:
                dano_jogador = 0
                if dado_jogador < 5 and dado_inimigo > 15:
                    dano_inimigo = 0
                elif dado_jogador < 15:
                    dano_inimigo = -(self.emocionalidade)
                else:
                    dano_inimigo = -(self.emocionalidade + 3)
        return dano_jogador, dano_inimigo
    #add frases e interações com as personalidades

    def fugir (self):
        self.energia -= 10
        return True if self.energia >= 50 else False

inventario = Inventário()
