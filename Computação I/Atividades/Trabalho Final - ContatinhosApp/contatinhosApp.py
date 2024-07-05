#Trabalho Final - ContatinhosApp - Parte 2 - Víctor BM
import os
import time
import contatinhosbib as cbib

contatos = []

def criar_contato():
    '''Função de interação para criar contato
    none -> none'''
    while True:
        print('Informe os dados conforme as perguntas. Caso queria não preencher um dado não obrigatório, pressionone enter\n')
        nome_criar = input('Informe o nome do seu contato: ')
        if nome_criar == '':
            os.system('cls')
            print('Você não informou o nome, que é obrigatório!\n')
            time.sleep(1)
        else:
            telefone_criar = input('Informe o telefone do seu contato: ')
            email_criar = input('Informe o email do seu contato: ')
            insta_criar = input('Informe o instagram do seu contato: ')
            os.system('cls')
            break
    return cbib.criar_contato(nome_criar, telefone_criar, email_criar, insta_criar)    

def main():
    print('--- Contatinhos App ---\n')
    print('Para fazer seu primeiro uso, é necessário criar um contato!')
    print('Para isso, é obrigatório informar um nome. Caso queria, pode informar telefone, email e instagram, respectivamente')
    contatos = [criar_contato()]
    cbib.contatos_geral = contatos
    while True:
        while True:
            print('Agora você pode acessar qualquer uma das 8 funcionalidades disponíveis no contatinhosApp')
            print('Você pode selecioná-las pelos códigos informados:\n\n0 -> Visualizar lista de contatos \n1 -> Criar contato\n2 -> Buscar contato')
            print('3 -> Atualizar Contato\n4 -> "Quem me ligou?"\n5 -> Excluir contato\n6 -> Aglutinar 2 contatos\n7 -> Sair\n')
            resposta = input('Qual funcionalidade você quer utilizar? ')
            if resposta in '01234567' and resposta != '':
                print('\n\n\n')
                resposta = int(resposta)
                break
            else:
                print('Funcionalidade inválida, tente novamente')
                time.sleep(2)
                os.system('cls')
        if resposta == 0:
            os.system('cls')
            print('Você selecionou a funcionalidade de visualizar lista de contatos')
            for element in contatos:
                print(element)
            print('\n')    
        elif resposta == 1:
            os.system('cls')
            print('Você selecionou a funcionalidade de criar contato')
            list. append(contatos, criar_contato())
            os.system('cls')
        elif resposta == 2:
            os.system('cls')
            print('Você selecionou a funcionalidade de buscar contato')
            nome = input('Digite um nome: ')
            resultado = cbib.buscar_contato(contatos, nome)
            for indice, infos in resultado:
                print(f'{indice} -> {infos}')
            print('\n\n\n')
        elif resposta == 3:
            print('Você selecionou a funcionalidade de atualizar contato')
            while True:
                contato_ind = input('Qual o índice correspondente ao contato a ser atualizado? ')
                if contato_ind in '0123456789' and contato_ind != '':
                    contato_ind = int(contato_ind)
                    if 0 <= contato_ind <= (len(contatos) - 1):
                        break
                    print('Índice inválido')
                else:
                    print('Índice inválido')
            print('0 -> nome; 1 -> telefones; 2 -> email, 3 -> instagram')
            while True:
                ind = input('Qual é o índice a ser atualizado? ')
                if ind in '0123456789' and ind != '': 
                    ind = int(ind)
                    if 0 <= ind <= 3:
                        break
                    print('Índice inválido')
                else:
                    print('Índice inválido')
            info = str(input('Qual informação a ser atualizada? '))
            if info == '' and ind != 0:
                os.system('cls')
                print('Você selecionou a opção de excluir uma informação do índice escolhido\nPossibilidades de exclusão: ')
                if type(contatos[contato_ind][ind]) is list:
                    for element in contatos[contato_ind][ind]:
                        print (element)
                else:
                    print(contatos[contato_ind][ind])
                info_apaga = input('Qual informação deve ser excluída? ')
                cbib.excluir_telefone(contatos[contato_ind], info_apaga)
            else:
                cbib.atualizar_contato(contatos[contato_ind], ind, info)
            os.system('cls')       
        elif resposta == 4:
            os.system('cls')
            print('Você selecionou a funcionalidade de "Quem me ligou?"')
            while True:
                ligacao = input('Qual foi o número que te ligou? ')
                if ligacao == '':
                    print('Número inexistente')
                else:
                    break
            pesquisa = cbib.quem_ligou(ligacao)
            if pesquisa == []:
                print('Desconhecido')
            else:
                print(pesquisa)
            input('Pressione enter para prosseguir')#apenas para a pessoa poder ver a resposta antes da tela ser limpa
            os.system('cls')
        elif resposta == 5:
            print('Você selecionou a funcionalidade de excluir contato')
            while True:
                contato_ind = input('Qual o índice correspondente ao contato a ser excluído? ')
                if contato_ind in '0123456789' and contato_ind != '':
                    contato_ind = int(contato_ind)
                    if 0 <= contato_ind <= (len(contatos) - 1):
                        break
                    print('Índice inválido')
                else:
                    print('Índice inválido')
            cbib.excluir_contato(contatos, contato_ind)
            os.system('cls')
            if len(contatos) == 0:
                print('Para utilizar o aplicativo, é necessário a existência de um contato!')
                contatos = [criar_contato()]
                cbib.contatos_geral = contatos
        elif resposta == 6:
            print('Você selecionou a funcionalidade de aglutinar 2 contatos')
            while True:
                contato_ind = input('Qual o índice correspondente do primeiro contato para aglutinar? ')
                if contato_ind in '0123456789' and contato_ind != '':
                    contato_ind = int(contato_ind)
                    break
                else:
                    print('Índice inválido')
            while True:
                contato_ind2 = input('Qual o índice correspondente do segundo contato para aglutinar? ')
                if contato_ind2 in '0123456789' and contato_ind2 != '':
                    contato_ind2 = int(contato_ind2)
                    break
                else:
                    print('Índice inválido')
            cbib.aglutinador(contatos, contato_ind, contato_ind2)
            os.system('cls')  
        else:
            encerrador = 5*['o o o']
            os.system('cls')
            print('Você selecionou a funcionalidade para encerrar o programa')
            time.sleep(1) 
            os.system('cls')  
            for h in range(5):
                print('Encerrando\n') #dando um charme a mais para o programa
                encerrador[h] = '- - -'
                for g in range(5):
                    print(encerrador[g])
                time.sleep(1)
                os.system('cls')
            print('Programa Encerrado!')
            time.sleep(1)
            break
main()
