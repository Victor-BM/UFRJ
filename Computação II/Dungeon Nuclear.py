#Trabalho Dungeon Nuclear

import os
from random import randint
from random import choice



class Personagem:
    def __init__(self,forca,agilidade,sorte):
        #self.verificar_atributos(forca,agilidade,sorte)
        self.forca = int(forca)
        self.agilidade = int(agilidade)
        self.sorte = int(sorte)
        self.vida = 100      
        self.lutando = False #adicionar o self.lutando nos lugares que precisa #talvez ja esteja certo
        self.arma = 'barra de chumbo' #talvez esses trco de equipamento suma
        self.defesa = []
        self.irradiado = 1
        self.chaves = 0


    def atacar(self,entidade):
        if not self.lutando:
            print('Nao ha nenhum inimigo para atacar.')
            #inimigo.recebeu_ataque()
            #self.finalizou_turno

    def rezar(self):
        deu_certo = False
        if self.sorte == 3:
            num_sorte = randint(1,5)
        elif self.sorte == 2:
            num_sorte = randint(1,10)
        elif self.sorte == 1:
            num_sorte = randint(1,15)
        else:
            num_sorte = randint(1,20)
        if num_sorte == 1:
            deu_certo = True

        if self.lutando and ('fuso_fissao' in sala_de_combate.entidades_na_sala):
            if deu_certo:
                print('Voce rezou mas...Meu deus!!! Parece que voce, de alguma forma, atingiu o fuso_fissao e ele ficou atordoado!')
                fuso_fissao.vida -= 30
                if fuso_fissao.vida <= 0:
                    print('Voce conseguiu derrotar o FUSO_FISSAO rezando! Que loucura!')
                    self.lutando = False
                    fuso_fissao.recebeu_ataque()
                else:
                   print('Ainda eh sua vez!')
                   self.iniciou_turno()
            else:
                print('Voce rezou mas parece que nada aconteceu...Voce perdeu o turno.')
                self.finalizou_turno()

        elif self.lutando:
            if deu_certo:
                print('Voce rezou mas...Meu deus!!! Parece que, de alguma forma, voce derrotou todos os inimigos da sala!')
                for entidade in sala_de_combate.entidades_na_sala:
                    if entidade in ['contaminante','emissor','derretedor','supernova']:
                        list.remove(sala_de_combate.entidades_na_sala,entidade)
                self.lutando = False
                self.iniciou_turno()
            else:
                print('Voce rezou mas parece que nada aconteceu...Voce perdeu o turno.')
                self.finalizou_turno()

        elif 'player' in sala_de_regeneracao.entidades_na_sala:
            if deu_certo:
                print('Parece que...algo mudou...')
                sala_de_regeneracao.maior_regeneracao = True #pedir pro peixoto adicionar isso
                self.iniciou_turno()
                
            else:
                print('Sera que...algo mudou...?')
            self.iniciou_turno()

        else:
            print('Voce rezou mas sera que algo mudou...?')
            self.iniciou_turno()
                

    def ver_vida(self):
        if self.vida <= 0:
            sala.resetar_tudo_player_morreu()
        elif 0 < self.vida <= 15:
            print(f'->Voce esta em estado crítico. Voce possui {self.vida} de vida. FUJA!')
        elif 15 < self.vida <= 30:
            print(f'->Muito cuidado! Voce possui {self.vida} de vida.')
        elif 30 < self.vida <= 60:
            print(f'->Sua vida esta mais baixa mas nao eh o fim. Voce possui {self.vida} de vida.')
        elif 60 < self.vida <= 90:
            print(f'->Voce tem alguns arranhoes. Voce possui {self.vida} de vida.')
        else:
            print(f'->Voce esta saudavel. Voce possui {self.vida} de vida.')


    #def iniciou_o_jogo  colocar coisas como: voce entra, qual os atributos do seu personagem
            #essa funcao precisa ser fora das classes pq nao vai ter player ainda
            #peixoto fez


    def entrar_numa_sala(self):
        numero_1a6 = randint(1,6)
        if numero_1a6 <= 3:
            sala_aleatoria = 'sala_de_combate'
        elif 4 <= numero_1a6 <= 5:
            sala_aleatoria = 'sala_de_bau'
        else:
            sala_aleatoria = 'sala_de_regeneracao'

        if sala_aleatoria == 'sala_de_combate':
            print('Voce entrou em combate!')
            list.append(sala_de_combate.entidades_na_sala,'player')
            sala_de_combate.spawnar_inimigos()
            self.lutando = True

        elif sala_aleatoria == 'sala_de_bau':
            list.append(sala_de_bau.entidades_na_sala,'player') #ver se precisa adicionar bau aqui

        else:
            list.append(sala_de_regeneracao.entidades_na_sala,'player')

        self.iniciou_turno()


    def iniciou_turno(self):  #colocar isso onde precisar
        print('\n--Seu Turno--\n')
        if self.lutando and ('fuso_fissao' in sala_de_combate.entidades_na_sala):
            print('--Derrote Fuso_fissao--')
            while True:
                print('O que voce deseja fazer agora?\n1- Atacar\n2- Ver vida\n3- Rezar\n4- Morrer\nNao se pode fugir desse desafio. Somente desistir.\n->Selecione um numero.\n')
                decisao = input()
                if decisao not in ('1','2','3','4'):
                    print('Selecione um numero valido.\n')
                else:
                    break

            if decisao == '1':
                print('Voce tenta atacar o fuso_fissao.')
                self.atacar('fuso_fissao') #depois ver se eh so isso mesmo

            elif decisao == '2':
                self.ver_vida()
                self.iniciou_turno()

            elif decisao == '3':
                self.rezar()

            else:
                print('Faz sentido. Fuso_fissao eh implacavel. Talvez essa nao tenho sido uma ma escolha...')
                self.vida = 0
                self.ver_vida()
                

        elif self.lutando:
            print('--Derrote os inimigos--')
            while True: 
                print('O que voce deseja fazer agora?\n1- Atacar\n2- Ver vida\n3- Rezar\n4- Fugir\n5- Morrer\n->Selecione um numero.\n')
                decisao = input()
                if decisao not in ('1','2','3','4','5'):
                    print('Selecione um numero valido.\n')
                else:
                    break

            if decisao == '1':
                while True:
                    print('Qual inimigo voce vai atacar?')
                    conta_opcoes = 1
                    for entidade in sala_de_combate.entidades_na_sala:
                        if entidade in ['contaminante','emissor','derretedor','supernova']:
                            print(f'{conta_opcoes}- Atacar {entidade}')
                            conta_opcoes += 1
                    print(f'{conta_opcoes}- Voltar\n->Selecione um numero.')
                    decisao_ataque = input()
                    lista_numeros_str = []
                    for numero in list(range(conta_opcoes+1)):
                        list.append(lista_numeros_str,str(numero))
                    if decisao_ataque not in lista_numeros_str:
                        print('Selecione um numero valido.\n')
                    else:
                        break
                novo_conta_opcoes = 0
                for entidade in sala_de_combate.entidades_na_sala:
                    if entidade in ['contaminante','emissor','derretedor','supernova']:
                        novo_conta_opcoes += 1
                        if decisao_ataque == str(conta_opcoes): 
                            print('Voltando...')
                            self.iniciou_turno()
                        elif decisao_ataque == str(novo_conta_opcoes):
                            self.atacar(entidade)
                            break #ver se esse break ta certo

            elif decisao == '2':
                self.ver_vida()
                self.iniciou_turno()

            elif decisao == '3':
                self.rezar()

            elif decisao == '4':
                if self.vida >= 50:
                    print('Ih...fugindo com tanta vida... Mas os inimigos ainda vao tentar te atacar...')
                else:
                    print('Voce vai tentar fugir. Mas os inimigos tambem vao tentar te atacar...')
                for entidade in sala_de_combate.entidades_na_sala:
                    if entidade in ['contaminante','emissor','derretedor','supernova']:
                        eval(entidade).escolha_de_ataque()
                print('Voce escapou do combate e da sala onde voce estava.')
                self.lutando = False
                list.clear(sala_de_combate.entidades_na_sala)
                self.iniciou_turno() #eh pra estar funcionando

            else:
                print('Voce decidiu morrer. Tudo bem...?')
                self.vida = 0
                self.ver_vida()
                

        else:
            if 'player' in sala_de_regeneracao.entidades_na_sala:
                print('Voce esta em uma sala estranha.\nVoce ve cruzes vermelhas e um motor nuclear que parece alimentar essa sala.')
                while True:
                    print('O que voce deseja fazer agora?\n1- Ligar o motor\n2- Ver vida\n3- Rezar\n4- Sair da sala\n5- Morrer\n->Selecione um numero.\n')
                    decisao = input()
                    if decisao not in ('1','2','3','4','5'):
                        print('Selecione um numero valido.\n')
                    else:
                        break

                if decisao == '1':
                    print('Ao ligar o motor, parece que a sala toda se ilumina e voce percebe que ela eh uma enfermaria.\nVoce vai poder se curar.')
                    sala_de_regeneracao.regenerar() 
                    self.iniciou_turno()

                elif decisao == '2':
                    self.ver_vida()
                    self.iniciou_turno()

                elif decisao == '3':
                    self.rezar()

                elif decisao == '4':
                    print('Voce decide sair da enfermaria.')
                    list.clear(sala_de_regeneracao.entidades_na_sala)
                    self.iniciou_turno()

                else:
                    print('Voce decidiu morrer. Tudo bem...?')
                    self.vida = 0
                    self.ver_vida()
                       

            elif 'player' in sala_de_bau.entidades_na_sala:
                    print('Aparentemente ha um conteiner nessa sala.')
                    while True:
                        print('O que voce deseja fazer agora?\n1- Olhar o conteiner\n2- Ver vida\n3- Rezar\n4- Sair da sala\n5- Morrer\n->Selecione um numero.\n')
                        decisao = input()
                        if decisao not in ('1','2','3','4','5'):
                            print('Selecione um numero valido.\n')
                        else:
                            break

                    if decisao == '1':
                        sala_de_bau.abrir_bau() #tem que ter iniciou_turno() lá ou aqui

                    elif decisao == '2':
                        self.ver_vida()
                        self.iniciou_turno()

                    elif decisao == '3':
                        self.rezar()

                    elif decisao == '4':
                        print('Voce decide sair da sala com o conteiner.')
                        list.clear(sala_de_bau.entidades_na_sala)
                        self.iniciou_turno()

                    else:
                        print('Voce decidiu morrer. Tudo bem...?')
                        self.vida = 0
                        self.ver_vida()


            elif 'player' in sala_de_combate.entidades_na_sala:
                print('Voce derrotou todos os inimigos. Parece que eles deixaram cair algo no chao.')
                while True:
                    print('O que voce deseja fazer agora?\n1- Pegar o objeto no chao\n2- Ver vida\n3- Rezar\n4- Sair da sala\n5- Morrer\n->Selecione um numero.\n')
                    decisao = input()
                    if decisao not in ('1','2','3','4','5'):
                        print('Selecione um numero valido.\n')
                    else:
                        break

                if decisao == '1':
                    if not sala_de_combate.pegou_chave:
                        if self.chaves == 0:
                            print('Parece que um dos inimigos tinha uma chave com ele.\nVoce deve precisar de mais chaves de acesso para vencer esse desafio.')
                        print('Voce pega a chave do chao.')
                        self.chaves += 1
                        sala_de_combate.pegou_chave = True
                        self.iniciou_turno()
                    else:
                        print('Voce ja pegou a chave do chao.')
                        self.iniciou_turno()

                elif decisao == '2':
                    self.ver_vida()
                    self.iniciou_turno()

                elif decisao == '3':
                    self.rezar()

                elif decisao == '4':
                    print('Voce decide sair da sala onde voce lutou.')
                    list.clear(sala_de_combate.entidades_na_sala)
                    sala_de_combate.pegou_chave = False
                    self.iniciou_turno()

                else:
                    print('Voce decidiu morrer. Tudo bem...?')
                    self.vida = 0
                    self.ver_vida()


            else:
                print('Voce esta vagando pela usina nuclear...')
                while True:
                    print('O que voce deseja fazer agora?\n1- Entrar em uma sala\n2- Ver vida\n3- Rezar\n4- Morrer\n->Selecione um numero.\n')
                    print(getattr(player,'forca'))
                    decisao = input()
                    if decisao not in ('1','2','3','4'):
                        print('Selecione um numero valido.\n')
                    else:
                        break

                if decisao == '1':
                    print('Voce esta entrando em uma sala misteriosa...')
                    self.entrar_numa_sala() 

                elif decisao == '2':
                    self.ver_vida()
                    self.iniciou_turno()

                elif decisao == '3':
                    self.rezar()

                else:
                    print('Voce decidiu morrer. Tudo bem...?')
                    self.vida = 0
                    self.ver_vida()       

        
            
    def finalizou_turno(self): #colocar isso onde precisar
        if self.irradiado > 0:
            self.vida -= self.irradiado
            print(f'Voce recebeu {self.irradiado} de dano de radiacao.')
            self.irradiado -= 1
            self.ver_vida()

        if 'player' in sala_de_combate.entidades_na_sala:
            tem_inimigo = False
            for entidade in sala_de_combate.entidades_na_sala:
                if entidade in ['contaminante','emissor','derretedor','supernova','fuso_fissao']:
                    tem_inimigo = True
                    eval(entidade).escolha_de_ataque()
            if not tem_inimigo:
                self.lutando = False

        self.iniciou_turno()
                            #ver se quando ele mata na vida morre tudo mesmo ???
                            

class Inimigo:
    def __init__(self):
        self.forca = 1
        self.agilidade = 1
        self.vida = 20
        self.fator_aleatorio = randint(1,2)

    def alterar_fator_aleatorio(self):
        if f'{self.__class__.__name__.lower()}' == 'fuso_fissao':
            self.fator_aleatorio = randint(1,3)
        else:
            self.fator_aleatorio = randint(1,2)

    def escolha_de_ataque(self):
        self.alterar_fator_aleatorio()
        if f'{self.__class__.__name__.lower()}' == 'fuso_fissao':
            if self.fator_aleatorio == 1:
                self.ataque_1()
            elif self.fator_aleatorio == 2:
                self.ataque_2()
            else:
                self.ataque_3()
        elif f'{self.__class__.__name__.lower()}' == 'supernova':
            if self.preparacao == 2:
                self.ataque_2()
            self.preparacao += 1
            print('A supernova esta aquecendo...')
        elif f'{self.__class__.__name__.lower()}' == 'contaminante':
            self.ataque_1()
        else:
            if self.fator_aleatorio == 1:
                self.ataque_1()
            else:
                self.ataque_2()


    def ataque_1(self): 
    #if(f'{self.__class__.__name__.lower()}') in sala.entidades_na_sala):
        if player.agilidade > self.agilidade:
            minimo_para_golpe = 15
        elif player.agilidade == self.agilidade:
            minimo_para_golpe = 10
        else:
            minimo_para_golpe = 5 

        tentativa_de_golpe = randint(1,20)
        if tentativa_de_golpe >= minimo_para_golpe:
            dano = 5*self.forca
            player.vida -= dano
            print(f'{self.__class__.__name__} te deu um ataque comum. Voce recebeu {dano} de dano.')
            if f'{self.__class__.__name__.lower()}' in ['contaminante','emissor','fuso_fissao']:
                self.irradiar() 
                print(f'O ataque te irradiou! Voce esta com {player.irradiado} de radiacao.')
            player.ver_vida()
        else:
            print(f'Voce esquivou do ataque de um {self.__class__.__name__.lower()}.') 


    def recebeu_ataque(self):
        if self.vida <= 0:
            list.remove(sala_de_combate.entidades_na_sala,f'{self.__class__.__name__.lower()}')
            self.vida = eval(f'{self.__class__.__name__.lower()}_padrao').vida
            if f'{self.__class__.__name__.lower()}' in ['contaminante','emissor','derretedor','supernova']:
                print(f'Voce derrotou um {self.__class__.__name.lower()}')
            else:
                a = 1#funcao de player.completou_dungeon()
        else:
            player.finalizou_turno() #talvez isso nao deva ficar aqui e sim no final do ataque do player
            

class Radioativo(Inimigo):
    def __init__(self):
        Inimigo.__init__(self)
        self.agilidade = 2

    def irradiar(self):
        player.irradiado += 1


class Fervente(Inimigo):
    def __init__(self):
        Inimigo.__init__(self)
        self.forca = 2
        self.ativou_calor = False

    def recebeu_ataque(self):
        if self.vida <= 0:
            list.remove(sala.entidades_na_sala,f'{self.__class__.__name__.lower()}')
            self.vida = eval(f'{self.__class__.__name__.lower()}_padrao').vida
            self.forca = eval(f'{self.__class__.__name__.lower()}_padrao').forca
            self.ativou_calor = False
        elif not self.ativou_calor and (self.vida < eval(f'{self.__class__.__name__.lower}_padrao').vida):
            self.forca += 1
            self.ativou_calor = True
            print(f'Esse {self.__class__.__name__.lower} SOBREAQUECEU e esta mais forte!')
            player.finalizou_turno()
        else:
            player.finalizou_turno()



class Contaminante(Radioativo):
    def __init__(self):
        Radioativo.__init__(self)
        self.vida = 40
 

class Emissor(Radioativo):
    def __init__(self):
        Radioativo.__init__(self)


    def irradiar(self):
        player.irradiado += 2


    def ataque_2(self):
        '''Feixe de radiacao. Alem de dar dano e irradiar, aumenta em +1 o player.irradiado.'''
        if player.agilidade > self.agilidade:
            minimo_para_golpe = 15
        elif player.agilidade == self.agilidade:
            minimo_para_golpe = 10
        else:
            minimo_para_golpe = 5

        tentativa_de_golpe = randint(1,20)
        if tentativa_de_golpe >= minimo_para_golpe:
            dano = 1*self.forca
            player.vida -= dano
            self.irradiar()
            player.irradiado += 1
            print('Voce recebeu um feixe de radiacao de um emissor.')
            print(f'Voce recebeu {dano} de dano e esta com {player.irradiado} de radiacao.')
            player.ver_vida()
        else:
            print('Voce esquivou do feixe radioativo do emissor.')
            


class Derretedor(Fervente):
    def __init__(self):
        Fervente.__init__(self)


    def ataque_2(self):
        if player.agilidade > self.agilidade: #linha 520 isso so serve pra saber a linha
            minimo_para_golpe = 15
        elif player.agilidade == self.agilidade:
            minimo_para_golpe = 10
        else:
            minimo_para_golpe = 5

        tentativa_de_golpe = randint(1,20)
        if tentativa_de_golpe >= minimo_para_golpe:
            dano = 3*self.forca
            player.vida -= dano
            print(f'O derretedor usou derreter e te causou {dano} de dano.')
            if player.arma != '' and player.defesa != '':
                self.alterar_fator_aleatorio()
                if self.fator_aleatorio == 1:  #importante ver essa questao do equipamento
                    player.arma = ''
                    print('Alem disso, por conta do ataque, ele derreteu sua arma!')
                else:
                    player.defesa = ''
                    print('Alem disso, por conta do ataque, ele derreteu seu escudo!')
            elif player.arma != '':
                player.arma = ''
                print('Alem disso, por conta do ataque, ele derreteu sua arma!')
            elif player.defesa != '':
                player.defesa = ''
                print('Alem disso, por conta do ataque, ele derreteu seu escudo!')
            else:
                mais_dano = 2*self.forca
                player -= mais_dano
                print('Alem disso, por conta do ataque, e por voce nao ter equipamento, ele tentou te derreter!')
                print(f'Voce recebeu mais {mais_dano} de dano.')
            player.ver_vida()
        else:
            print('Voce esquivou do ataque de derretimento do derretedor.')
            

class Supernova(Fervente):
    def __init__(self):
        Fervente.__init__(self)
        self.vida = 15
        self.preparacao = 0


    def ataque_2(self):
        if player.agilidade > self.agilidade:
            minimo_para_golpe = 7
        elif player.agilidade == self.agilidade:
            minimo_para_golpe = 3
        else:
            minimo_para_golpe = 1

        tentativa_de_golpe = randint(1,20)
        if tentativa_de_golpe >= minimo_para_golpe:
            dano = 12*self.forca
            player -= dano
            print(f'A supernova EXPLODIU!!! Voce recebeu absurdos {dano} de dano!')
        else:
            dano = 1*self.forca
            player -= dano
            print(f'Voce conseguiu esquivar da maior parte do dano mais ainda recebeu {dano} de dano.')
        player.ver_vida()


class Fuso_fissao(Radioativo,Fervente):
    def __init__(self):
        Radioativo.__init__(self)
        Fervente.__init__(self)


    def ataque_2(self):
        if player.agilidade > self.agilidade:
            minimo_para_golpe = 15
        elif player.agilidade == self.agilidade:
            minimo_para_golpe = 10
        else:
            minimo_para_golpe = 5 


    def ataque_3(self):
        if player.agilidade > self.agilidade:
            minimo_para_golpe = 15
        elif player.agilidade == self.agilidade:
            minimo_para_golpe = 10
        else:
            minimo_para_golpe = 5 




'--------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------'


#quantidade_de_inimigos = randint(1,3)
#escolha = input('Voce encontrou uma porta. Deseja entrar? [S ou N]')
class Sala:
    def __init__(self):
        self.entidades_na_sala = []  


    def resetar_tudo_player_morreu(self):
        print('Sua vida chegou a 0.\nSua jornada nuclear chegou ao fim.\nVoce nao conquistou esse mundo. Va embora desse dominio. FIM.')
        list.clear(sala_de_regeneracao.entidades_na_sala)
        list.clear(sala_de_combate.entidades_na_sala)
        list.clear(sala_de_bau.entidades_na_sala)
        player.vida = 100 
        player.irradiado = 0
        player.chaves = 0
        player.lutando = False   #ver se precisa mexer mais coisas
        for fervente in ['derretedor','supernova','fuso_fissao']:
            eval(fervente).ativou_calor = False
        for inimigo in ['contaminante','emissor','derretedor','supernova','fuso_fissao']:
            eval(inimigo).forca = eval(f'{inimigo}_padrao').forca
            eval(inimigo).agilidade = eval(f'{inimigo}_padrao').agilidade
            eval(inimigo).vida = eval(f'{inimigo}_padrao').vida
        os.system('cls')
        #armas = []
        #defesa = []
        #colocar funcao pra voltar o jogo do inicio
        #ver se os atributos do personagem ficam normais depois
        


class Sala_de_combate(Sala):
    def __init__(self):
        Sala.__init__(self)


    def quantidade_de_inimigos(self):
        x = randint(1,3)
        return x
 
       
    def spawnar_inimigos(self):
        if player.chaves < 4: #esse numero pode mudar. Numero de batalhas antes do boss
            possiveis_inimigos = ['contaminante', 'supernova', 'emissor', 'derretedor']
            count = 0
            num_inimigos = self.quantidade_de_inimigos()
            print(f'Voce se deparou com {num_inimigos} inimigo(s)!') 
            while count < num_inimigos:
                self.entidades_na_sala.append(choice(possiveis_inimigos))
                count += 1
        else:
            list.append(self.entidades_na_sala,'fuso_fissao')
            print('Voce iniciou sua batalha contra Fuso_fissao.')


    #def desespawnar_inimigos(self):
       # for entidade in self.entidades_na_sala:
          #  if entidade in ['contaminante', 'supernova', 'emissor', 'derretedor']:
              #  if eval(entidade).vida <= 0:
            #        list.remove(self.entidades_na_sala, entidade)
                  #  eval(entidade).vida


class Sala_de_regeneracao(Sala):
    def __init__(self):
        Sala.__init__(self)
        self.maior_regeneracao = False

    
    def regenerar(self):
        if self.maior_regeneracao:
            player.vida += 50
            print('Suas preces foram ouvidas. Os deuses irão lhe retribuir pela sua fé!\nVoce regenerou 50 de vida!')
        else:
            player.vida += 30
            print('Voce sentiu uma energia fluindo pelo seu corpo.\nVoce recebeu 30 de vida!')
        #ajeitar para que a vida do personagem nao ultrapasse a vida maxima.
        #ver isso so depois de ver como os equipamentos vao afetar a vida
            #ajeitar para que so possa usar uma vez


class Sala_de_bau(Sala):
    def __init__(self):
        Sala.__init__(self)   


    def abrir_bau(self):
        escolha_do_bau = (input('Voce deparou-se com um bau misterioso dentro da sala. Deseja abri-lo? [S ou N]')).lower()
        if escolha_do_bau == 'n':
            print('Voce nao abriu o bau.')
            player.iniciou_turno()   #colocar condicao de se abriu bau uma vez nessa sala nao abre mais
        elif escolha_do_bau == 's':
            dentro_do_bau = randint(1,7)
            if dentro_do_bau <= 3:
                barras = randint(1,3)
                if barras == 1:
                    print('Voce encontrou uma barra de chumbo enferrujada.\n-Dano: 5- ')
                if barras == 2:
                    print('Voce encontrou uma barra de chumbo levemente desgastada.\n-Dano: 8- ')
                if barras == 3:
                    print('Voce encontrou uma barra de chumbo nova e reluzente.\n-Dano: 11- ')
            if 4 <= dentro_do_bau <= 6:
                escudos = randint(1,3)
                if escudos == 1:
                    print('Voce encontrou um escudo de madeira.\n-Defesa: 5-')
                if escudos == 2:
                    print('Voce encontrou um escudo de ferro.\n-Defesa: 15-')
                if escudos == 3:
                    print('Voce encontrou um escudo de chumbo potente.\n-Defesa: 30-')
            if dentro_do_bau == 7:
                player.vida -= 20
                print('O-o que? O bau era um mimico e te atacou!!\nVoce perdeu 20 de vida.')
                player.ver_vida()


def main():
    while True:
        print('--Bem vindo a cidade de Springfield, lar da grande e renomada família Simpsons.--\n')
        print('->Essa cidade é muito conhecida pelas pessoas, pelos lazeres e pontos turísticos mas também pela sua respeitosa Usina Nuclear que pertence ao ambicioso Sr. Burns.')
        print('->Não é mistério para ninguém que um de seus melhores empregados é Homer Simpson, um homem um tanto quanto desastrado.')
        print('->Em um dia, até então rotineiro, Homer esbarra em um botão escrito "NÃO APERTE! RISCO DE EXPLOSÃO !" dentro da sala de segurança do setor 7-G.')
        print('->Como é de se esperar, após 5 segundos do clique, a usina inteira vai para os ares assim como quase toda a cidade de Springfield.')
        print('->Você, um inspetor de desastres da cidade mais próxima, é chamado para investigar o acontecimento e é obrigado a visitar a cidade.')
        print('->Logo na entrada, você percebe o tamanho da destruição que ocorreu, que só aumenta ao entrar da cidade.')
        print('->Chegando na entrada da Usina, que nem mesmo parece mais uma, você encontra uma única porta não danificado, provavelmente seu único meio de entrar.\n')
        primeira_acao = (input('Você deseja entrar? [S ou N] ')).lower()
        if primeira_acao == 'n':
            os.system('cls')
            print('Você não foi corajoso o suficiente para enfrentar esse desafio e voltou para casa.')
            break
        else:
            print('->Você deve agora escolher os valores de seus atributos, sendo eles: força, agilidade e sorte.')
            print('->Digite respectivamente os valores indicados, podendo variar de 0 a 3, porém a soma dos atributos nao pode ultrapassar 3.')
            print('->EX: (Força: 1, Agilidade: 2, Sorte: 0), (Força: 3, Agilidade: 0, Sorte: 0), (Força: 1, Agilidade: 1, Sorte: 1)\n')
            while True:
                forca = (input('\nForça: '))
                agilidade = (input('Agilidade: '))
                sorte = (input('Sorte: '))
                confirmacao = False
                nums_possiveis = ('0','1','2','3')
                if not((forca in nums_possiveis) and (agilidade in nums_possiveis) and (sorte in nums_possiveis)):
                    print('Erro: um dos atributos nao eh um numero de 0 a 3. Digite novamente.')
                elif (int(forca) + int(agilidade) + int(sorte)) != 3:
                    print('Erro: a soma da forca, agilidade e sorte deve ser igual a 3. Digite novamente.')
                else:
                    confirmacao = True

                if confirmacao:
                    break
            player = Personagem(forca,agilidade,sorte)
            player.iniciou_turno()





contaminante = Contaminante()
emissor = Emissor()
derretedor = Derretedor()
supernova = Supernova()
fuso_fissao = Fuso_fissao()


contaminante_padrao = Contaminante()
emissor_padrao = Emissor()
derretedor_padrao = Derretedor()
supernova_padrao = Supernova()
fuso_fissao_padrao = Fuso_fissao()


sala = Sala()
sala_de_combate = Sala_de_combate()
sala_de_regeneracao = Sala_de_regeneracao()
sala_de_bau = Sala_de_bau()
#sala_de_combate.spawnar_inimigos()
#sala_de_bau.abrir_bau()
    
    
main()














