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
        nome_criar = input('Informe o nome do seu primeiro contato: ')
        if nome_criar == '':
            os.system('cls')
            print('Você não informou o nome, que é obrigatório!\n')
            time.sleep(1)
        else:
            telefone_criar = input('Informe o telefone do seu primeiro contato: ')
            email_criar = input('Informe o email do seu primeiro contato: ')
            insta_criar = input('Informe o instagram do seu primeiro contato: ')
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
            print('3 -> Atualizar Contato\n4 -> Quem te ligou?\n5 -> Excluir contato\n6 -> Aglutinar 2 contatos\n7 -> Sair\n')
            resposta = int(input('Qual funcionalidade você quer utilizar? '))
            if 0 <= resposta <= 8:
                break
            else:
                print('Funcionalidade inválida, tente novamente')
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
        elif resposta == 2:
            print('buscar contato')#implementar ainda
        elif resposta == 3: #verificar se ta correto ainda
            os.system('cls')
            print('Você selecionou a funcionalidade de atualizar contato')
            contato_ind = int(input('Qual o índice correspondente ao contato a ser atualizado? '))
            print('0 -> nome; 1 -> telefones; 2 -> email, 3 -> instagram')
            ind = int(input('Qual é o índice a ser atualizado? '))
            info = str(input('Qual informação a ser atualizada? '))
            if info == '':
                print('Você selecionou a opção de excluir uma informação do índice escolhido')
            cbib.atualizar_contato(contatos[contato_ind], ind, info)         
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








def teste():
    contatos = [['João Fields', [''], 'aa', ''], ['Ana Fieldson', [''], 'bb', '']]
    cbib.contatos_geral = contatos
    ind = 0
    print(cbib.buscar_contato(contatos, 'Fields'))
    cbib.atualizar_contato(contatos[ind], 2, 'cc')
    print(contatos)
    cbib.atualizar_contato(contatos[ind], 2, '')
    #print(contatos)
    cbib.excluir_telefone(contatos[ind],'12')
    contatos = cbib.contatos_geral
    print(contatos)
    #print(cbib.quem_ligou('37'))
    #cbib.criar_contato('Joana', '32323')
    #print(contatos)
    #cbib.excluir_contato(contatos, 2)
    #print(contatos)
    cbib.atualizar_contato(contatos[ind], 1, '11')
    cbib.excluir_telefone(contatos[ind],'cc')
    print(contatos)
    cbib.aglutinador(contatos, 0, 1)
    print(contatos)
teste()
