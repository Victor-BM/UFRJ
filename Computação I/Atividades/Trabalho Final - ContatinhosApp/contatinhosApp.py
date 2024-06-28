#Trabalho Final - ContatinhosApp - Parte 2 - Víctor BM
import os
import time
import contatinhosbib as cbib

contatos = []

def criar_contato():
    '''Função de interação para criar contato
    none -> none'''
    while True:
        print('Para isso, é obrigatório informar um nome. Caso queria, pode informar telefone, email e instagram, respectivamente')
        print('Informe os dados em str, por exemplo, ’joão’. Caso queria não preencher um dado não obrigatório, digite ''')
        nome_criar = eval(input('Informe o nome do seu primeiro contato: '))
        if nome_criar == '':
            os.system('cls')
            print('Você não informou o nome, que é obrigatório!\n')
            time.sleep(1)
        else:
            telefone_criar =  eval(input('Informe o telefone do seu primeiro contato: '))
            email_criar =  eval(input('Informe o email do seu primeiro contato: '))
            insta_criar =  eval(input('Informe o instagram do seu primeiro contato: '))
            os.system('cls')
            break
    return cbib.criar_contato(nome_criar, telefone_criar, email_criar, insta_criar)

def main():
    print('--- Contatinhos App ---')
    print('Para fazer seu primeiro uso, é necessário criar um contato!')
    contatos = [criar_contato()]
    cbib.contatos_geral = contatos
    while True:
        while True:
            print('Agora você pode acessar qualquer uma das 8 funcionalidades disponíveis no contatinhosApp')
            print('Você pode selecioná-las pelos códigos informados:\n0 -> Criar contato // 1 -> Atualizar contato // 2 -> Excluir telefone')
            print('3 -> Buscar contato // 4 -> Quem te ligou? // 5 -> Excluir contato // 6 -> Aglutinar 2 contatos // 7 -> Visualizar lista de contatos')
            resposta = int(input('Qual funcionalidade você quer utilizar? '))
            if 0 <= resposta <= 8:
                break
            else:
                print('Funcionalidade inválida, tente novamente')
        if resposta == 0:
            os.system('cls')
            print('Você selecionou a funcionalidade de criar contato')
            list. append(contatos, criar_contato())
        elif resposta == 1:
            os.system('cls')
            print('Você selecionou a funcionalidade de atualizar contato')
            contato_ind = int(input('Qual o índice correspondente ao contato a ser atualizado? '))
            print('0 -> nome; 1 -> telefones; 2 -> email, 3 -> instagram')
            ind = int(input('Qual é o índice a ser atualizado? '))
            info = str(input('Qual informação a ser atualizada? '))
            cbib.atualizar_contato(contatos[contato_ind], ind, info)
        else: #seria o 8 aq, lembrar q tá pouco pq ainda n coloquei as outras
            os.system('cls')
            print('Você selecionou a funcionalidade de visualizar lista de contatos')
            for element in contatos:
                print(element)
            print('\n')                








def teste():
    contatos = [['João Fields', [''], 'aa', ''], ['Ana Fieldson', [''], 'bb', '']]
    cbib.contatos_geral = contatos
    ind = 0
    print(cbib.buscar_contato(contatos, 'Fields'))
    cbib.atualizar_contato(contatos[ind], 2, '')
    print(contatos)
    #cbib.excluir_telefone(contatos[ind],'12')
    #contatos = cbib.contatos_geral
    #print(contatos)
    print(cbib.quem_ligou('37'))
    cbib.criar_contato('Joana', '32323')
    print(contatos)
    #cbib.excluir_contato(contatos, 2)
    #print(contatos)
    cbib.aglutinador(contatos, 0, 1)
    print(contatos)
main()
