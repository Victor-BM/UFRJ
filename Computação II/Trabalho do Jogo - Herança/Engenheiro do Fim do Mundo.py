import random
import docs
import base
import time
import os

inventario = base.inventario
monstro = base.Monstros()
item_drop = base.Item()

def gera_items():
        item_drop.tipo = random.choice(['vida', 'sanidade'])
        item_drop.disponibilidade = random.randint(5, 10)
        if item_drop.tipo == 'vida':
            aleatorio = random.randint(1, 3)
            if aleatorio == 1:
                item_drop.nome = 'Esparadrapo'
                item_drop.descrição = 'Simples e útil'
            elif aleatorio == 2:
                item_drop.nome = 'Babosa'
                item_drop.descrição = 'Cura até fratura exposta :O'
            else:
                item_drop.nome = 'Células Regenerativas'
                item_drop.descrição = 'Uma dose de avanço científico '
        else:
            aleatorio = random.randint(1, 3)
            if aleatorio == 1:
                item_drop.nome = 'Ursinho de Pelúcia'
                item_drop.descrição = 'Assim como acalmou alguém no passado, agora te acalma também'
            elif aleatorio == 2:
                item_drop.nome = 'Summer EletroHits 2005'
                item_drop.descrição = 'Uma coletânea maravilhosa que regenera tua mente'
            else:
                item_drop.nome = 'Cerveja Bavária - Edição Colapso Global'
                item_drop.descrição = 'BIZARRO. É tão absurdamente ruim que é capaz de inverter o efeito de perda de sanidade'
            
def gera_monstros():
    aleatorio = random.choices(['Lobo-Barata', 'Mutante', 'Amálgama de Corpos', 'Aberração Biológica', 'Devorador de Almas'], weights = [10, 8, 3, 2, 1], k = 1)
    monstro.espécie = aleatorio[0]
    monstro.estado = True
    monstro.vida = monstro.vida_máx
    monstro.energia = monstro.energia_máx
    monstro.debuff_vida()
    if monstro.espécie == 'Lobo-Barata':
        monstro.fisicalidade = random.randint(0,3)
        monstro.racionalidade = random.randint(0, 3)
        monstro.emocionalidade = random.randint(0, 3)
    elif monstro.espécie == 'Mutante':
        monstro.fisicalidade = random.randint(2,5)
        monstro.racionalidade = random.randint(2,5)
        monstro.emocionalidade = random.randint(2,5)
    elif monstro.espécie == 'Amálgama de Corpos':
        monstro.fisicalidade = random.randint(3, 8)
        monstro.racionalidade = random.randint(3, 8)
        monstro.emocionalidade = random.randint(3, 8)
    elif monstro.espécie == 'Aberração Biológica':
        monstro.fisicalidade = random.randint(4,15)
        monstro.racionalidade = random.randint(4, 15)
        monstro.emocionalidade = random.randint(4, 15)
    elif monstro.espécie == 'Devorador de Almas':
        monstro.fisicalidade = random.randint(4,20)
        monstro.racionalidade = random.randint(4, 20)
        monstro.emocionalidade = random.randint(4, 20)    

def main():
    print(docs.introdução)

    while True:
        fisicalidade, racionalidade, emocionalidade = eval(input('Você tem 20 pontos de atributo.\nDigite os acréscimos de atributos. Exemplo -> [3, 5, 12]: '))
        if isinstance(fisicalidade, int) and isinstance(racionalidade, int) and isinstance(racionalidade, int) and ((fisicalidade + racionalidade + emocionalidade) == 20):
            jogador = base.Jogador(fisicalidade, racionalidade, emocionalidade)
            vozes = docs.Personalidades(fisicalidade, racionalidade, emocionalidade)
            os.system('cls')
            print('Preparade para arrebentar a boca do balão?\n\n\n')
            break
        else:
            os.system('cls')
            print('Valores inválidos! Exemplo -> [3, 5, 12]')
    print(docs.texto_saida_bunker)
    
    while True:
        decisao_bunker = int(input("O que você quer fazer?\n1. Continuar explorando o apocalipse\n2. Voltar correndo para o buncker: \n"))
        if decisao_bunker == 1 and isinstance(decisao_bunker, int):
            print("Você tomou coragem e decide encarar o fim do mundo. É difícil respirar e você tem a sensação de que alguém está te observando.")    
            break
        elif decisao_bunker == 2 and isinstance(decisao_bunker, int):
            print("É melhor se preparar e voltar depois. Você corre para o bunker e.. AH NÃO, ELE FECHOU! Como você vai enfrentar criaturas mutantes agora?")
            break
        else:
            print("Você está no fim do mundo e ainda erra a escolha? Parabéns! Talvez seja por isso que apertou aquele botão vermelho. Escolha 1 ou 2.")
    time.sleep(3)
    os.system('cls')
    print(docs.texto_evento_1)

    while True:
        decisao_supermercado = int(input("O que você quer fazer?\n1. Entrar no supermercado\n2. Ignorar e continuar andando: \n"))
        if decisao_supermercado == 1 and isinstance(decisao_supermercado, int):
            print("Você entra no supermercado e fica surpreso por ainda ter alimentos nas prateleiras. Você está animado com o local, mas... algo está se movendo NA SUA DIREÇÃO!") 
            time.sleep(3)
            print('Ufa, ainda bem que você é capaz de correr, mas, no susto, acabou batendo o dedinho na quina da prateleira!')   
            jogador.se_machucar(-5)
            break
        elif decisao_supermercado == 2 and isinstance(decisao_supermercado, int):
            print("Você decide ignorar o supermercado e continua andando. Mas então, que som é esse? Você escuta passos mas não os localiza!")
            jogador.perder_sanidade('desconexão')
            jogador.debuff_sanidade()
            break
        else:
            print("Você está no fim do mundo e ainda erra a escolha? Parabéns! Talvez seja por isso que apertou aquele botão vermelho. Escolha 1 ou 2.")
    time.sleep(3)
    os.system('cls')

    while (jogador.dia < 21 and jogador.estado == True):
        while True:
            print(f'--- Dia: {jogador.dia} ----')
            print('E agora?\n0 -> Exibir Status\n1 -> Olhar Inventário\n2 -> Explorar\n3 -> Descansar\n4 -> Se curar\n5 -> Recuperar Sanidade\n6 -> Remover Item')
            resposta = int(input('O que você deseja fazer? '))
            print('\n')
            if resposta == 0 and isinstance(resposta, int):
                jogador.ficha()
                print('\n')
            elif resposta == 1 and isinstance(resposta, int):
                inventario.listar_items()
            elif resposta == 2 and isinstance(resposta, int):
                vozes.gerar_frase_aleatoria()
                jogador.explorar()
                aleatorio = random.choices(['monstro', 'item', 'sanidade'], weights = [8, 2, 1], k = 1)
                if aleatorio[0] == 'item':
                    gera_items()
                    print('Você encontrou um item!')
                    item_drop.exibir_informação
                    escolha = input('Você deseja adicionar esse item ao seu inventário? [S ou N]: ').lower()
                    if escolha == 's' and isinstance(escolha, str):
                        inventario.adicionar_item(item_drop)
                    else:
                        print('Item não adicionado!')        
                elif aleatorio[0] == 'sanidade':
                    jogador.perder_sanidade()
                    jogador.debuff_sanidade()
                else:
                    gera_monstros()
                    break
            elif resposta == 3 and isinstance(resposta, int):
                horas = int(input('Quantas horas você deseja descansar? '))
                dano_fisico, dano_mental = jogador.descansar(horas)
                jogador.se_machucar(dano_fisico)
                jogador.perder_sanidade(dano_mental)
                jogador.debuff_sanidade()
            elif resposta == 4 and isinstance(resposta, int):
                inventario.listar_items()
                ind = int(input('Escolha um item pela sua posição no inventário (0 a 4): '))
                if (0 <= ind < (len(inventario.items))) and len(inventario.items) != 0:
                    jogador.curar(inventario.items[ind])
            elif resposta == 5 and isinstance(resposta, int):
                inventario.listar_items()
                ind = int(input('Escolha um item pela sua posição no inventário (0 a 4): '))
                if (0 <= ind < (len(inventario.items))) and len(inventario.items) != 0:
                    print('2')
                    jogador.recuperar_sanidade(inventario.items[ind])
            elif resposta == 6 and isinstance(resposta, int):
                inventario.listar_items()
                ind = int(input('Escolha um item pela sua posição no inventário (0 a 4): '))
                if (0 <= ind < (len(inventario.items))) and len(inventario.items) != 0:
                    inventario.remover_item(inventario.items[ind])
            print('\n\n\nAperte Enter para prosseguir')
            input()
            os.system ('cls')
        while jogador.estado == True:
            print(f'Você encontrou um {monstro.espécie}. Você vai se acorvadar ou vai tentar exterminá-lo?')
            escolha = int(input('Digite 1 para fugir ou 2 para combater: '))
            if escolha == 1 and isinstance(escolha, int):
                print('O medo de morrer te dominou, não é mesmo?')
                possibilidade = jogador.fugir()
                if possibilidade:
                    break
                else:
                    print('Você não possui energia o suficiente para fugir. Prepara-se para lutar!')
                    escolha = 2
            if escolha == 2 and isinstance(escolha, int):
                print('A luta por sobrevivência começa agora...')
                print('Você pode lutar de 3 maneiras: Fisicalidade, Racionalidade e Emocionalidade')
                while jogador.estado == True and monstro.estado == True:
                    modo_luta = int(input('Digite 1 para Fisicalidade, 2 para Racionalidade e 3 para Emocionalidade: '))
                    if modo_luta == 1 and isinstance(modo_luta, int):
                        vozes.frase_combate('fisicalidade')
                        dano_jogador, dano_inimigo = jogador.combater(monstro, 'fisicalidade')
                        jogador.se_machucar(dano_jogador)
                        monstro.se_machucar(dano_inimigo)
                        monstro.debuff_vida()
                    elif modo_luta == 2 and isinstance(modo_luta, int):
                        vozes.frase_combate('racionalidade')
                        dano_jogador, dano_inimigo = jogador.combater(monstro, 'racionalidade')
                        jogador.se_machucar(dano_jogador)
                        monstro.se_machucar(dano_inimigo)
                        monstro.debuff_vida()
                    elif modo_luta == 3 and isinstance(modo_luta, int):
                        vozes.frase_combate('emocionalidade')
                        dano_jogador, dano_inimigo = jogador.combater(monstro, 'emocionalidade')
                        jogador.se_machucar(dano_jogador)
                        monstro.se_machucar(dano_inimigo)
                        monstro.debuff_vida()
                    if dano_jogador == 0 and dano_inimigo == 0:
                        print('Matéria e Anti-Matéria se cancelam, bem lembrado')
                    elif dano_jogador == 0 and dano_inimigo < 0:
                        print('Wow, até parece que você sabe lutar')
                    else:
                        print('Essa doeu T-T')
                    if jogador.vida < 30:
                        print('Você se sente muito fraco, uma sensação indescritível... Você está próximo da morte!')
                    print(f'Sua vida: {jogador.vida}')
                    print(f'Vida do inimigo: {monstro.vida}')
                    print('\n\n\nAperte Enter para prosseguir')
                    input()
                    os.system ('cls')
                if not monstro.estado:
                    print('tchau tchau bau bau bicho feio')
                    print('Você sai todo capenga, mas A luta trouxe suas recompensas!')
                    gera_items()
                    print('A besta carregava um item, agora você pode coletar os espólios de guerra!')
                    item_drop.exibir_informação
                    escolha = input('Você deseja adicionar esse item ao seu inventário? [S ou N]: ').lower()
                    if escolha == 's' and isinstance(escolha, str):
                        inventario.adicionar_item(item_drop)
                    else:
                        print('Item não adicionado!')
                    print('\n\n\nAperte Enter para prosseguir')
                    input()
                    os.system ('cls')
                    break
            else:
                print('\nVocê está no fim do mundo e ainda erra a escolha? Parabéns! Talvez seja por isso que apertou aquele botão vermelho. Escolha 1 ou 2.')
    time.sleep(3)
    os.system('cls')
    if jogador.estado == False:
        print(docs.texto_derrota)
    elif jogador.dia >= 21:
        print(docs.texto_vitoria)
    print('\n')
    print(docs.texto_agradecimento)
    print('\n\n\nAperte Enter para prosseguir')
    input()
    os.system ('cls')
if __name__ == '__main__':
    main()