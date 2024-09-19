import random
import docs
import base
import time
import os

def main():
    print(docs.introdução)
    while True:
        fisicalidade, racionalidade, emocionalidade = eval(input('Digite os acréscimos de atributos: '))
        if isinstance(fisicalidade, int) and isinstance(racionalidade, int) and isinstance(racionalidade, int) and ((fisicalidade + racionalidade + emocionalidade) == 20):
            jogador = base.Jogador(fisicalidade, racionalidade, emocionalidade)
            inventario = base.Inventário()
            monstro = base.Monstros('vazio', 0, 0, 0)
            os.system('cls')
            print('Preparade para arrebentar a boca do balão?\n\n\n')
            break
        else:
            os.system('cls')
            print('Valores inválidos! Exemplo -> [3, 5, 12]')
    print(docs.texto_saida_bunker)
    
    while True:
        decisao_bunker = input("\nO que você quer fazer?\n1. Continuar explorando o apocalipse\n2. Voltar correndo para o buncker: \n")
        if decisao_bunker == "1":
            print("\nVocê tomou coragem e decide encarar o fim do mundo. É difícil respirar e você tem a sensação de que alguém está te observando.")    
            break
        elif decisao_bunker == "2":
            print("\nÉ melhor se preparar e voltar depois. Você corre para o bunker e.. AH NÃO, ELE FECHOU! Como você vai enfrentar criaturas mutantes agora?")
            break
        else:
            print("\nVocê está no fim do mundo e ainda erra a escolha? Parabéns! Talvez seja por isso que apertou aquele botão vermelho. Escolha 1 ou 2.")
        time.sleep(3)
        os.system('cls')
    print(docs.texto_evento_1)

    while True:
        decisao_supermercado = input("\nO que você quer fazer?\n1. Entrar no supermercado\n2. Ignorar e continuar andando: \n")
        if decisao_supermercado == "1":
            print("\nVocê entra no supermercado e fica surpreso por ainda ter alimentos nas prateleiras. Você está animado com o local, mas... algo está se movendo NA SUA DIREÇÃO")    
            break
        elif decisao_supermercado == "2":
            print("\nVocê decide ignorar o supermercado e continua andando. Mas então, que som é esse? São passos e estão te seguindo!")
            break
        else:
            print("\nVocê está no fim do mundo e ainda erra a escolha? Parabéns! Talvez seja por isso que apertou aquele botão vermelho. Escolha 1 ou 2.")
    
    while (jogador.dia < 21 and jogador.estado == True):
        while True:
            print('E agora?\n0 -> Exibir Status\n1 -> Olhar Inventário\n2 -> Explorar\n3 -> Descansar\n4 -> Se curar\n5 -> Recuperar Sanidade\n6 -> Remover Item')
            resposta = int(input('O que você deseja fazer? '))
            if resposta == 0:
                jogador.ficha()
            elif resposta == 1:
                inventario.listar_items()
            elif resposta == 2:
                jogador.explorar()
                #gerar monstro ou gerar item
            elif resposta == 3:
                horas = int(input('Quantas horas você deseja descansar? '))
                jogador.descansar(horas)
            elif resposta == 4:
                inventario.listar_items()
                item = int(input('Escolha um item pela sua posição no inventário: '))
                if inventario[item] in inventario:
                    jogador.curar(inventario[item])
            elif resposta == 5:
                inventario.listar_items()
                item = int(input('Escolha um item pela sua posição no inventário: '))
                if inventario[item] in inventario:
                    jogador.recuperar_sanidade(inventario[item])
            elif resposta == 6:
                inventario.listar_items()
                item = int(input('Escolha um item pela sua posição no inventário: '))
                if inventario[item] in inventario:
                    inventario.remover_item(item)
        
        
if __name__ == '__main__':
    main()