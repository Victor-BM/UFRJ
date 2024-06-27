#Trabalho Final - ContatinhosApp - Parte 1 - Víctor BM
#contatos = []#colocar isso no arquivo de interfacd
def criar_contato (nome, telefone = '', email = '', instagram = ''):
    '''Função que permite criar contatos com apenas o nome obrigatório
    str, str, str, str -> list'''
    contato = []
    telefones = [telefone,]
    contato1 = [nome, telefones, email, instagram]
    list.append(contato, contato1)
    return contato

def atualizar_contato (contato, indice, nova_inf):
    '''Função que permite atualizar o contato adicionando uma nova informação pelo indice
    0 -> nome; 1 -> telefones; 2 -> email, 3 -> instagram
    list, int, str -> list'''
    if indice == 0 or indice == 2 or indice == 3:
        contato[indice] = nova_inf
    if indice == 1 and (nova_inf != contato[1]):
        contato[1] = [contato[1]]
        list.append(contato[1], nova_inf)
    contato = contato[::]
    return contato
    
def excluir_telefone (contato, telefone):
    '''Função que permite excluir o telefone do contato
    list, string -> list'''
    if telefone in contato[1]:
        list.remove(contato[1], telefone)
    return contato

def buscar_contato (contatos, nome):
    '''Função que busca um contato em uma lista de contatos
    list, str -> list'''
    i = 0
    resposta = []
    nome = nome.lower()
    while i<(len(contatos)):
        nome_contato = contatos[i][0]
        nome_contato = nome_contato.lower()
        if nome in nome_contato:
            resposta.append([i, contatos[i]])
        i += 1
    return resposta

def quem_ligou(contatos, ligacao):
    '''Função que retorna os dados de quem ligou
    list, str -> list'''
    for i in range(len(contatos)):
        if type(contatos[i][1]) is list:
            for j in range(len(contatos[i][1])):
                if ligacao in contatos[i][1][j]:
                    return contatos[i]
        if ligacao in contatos[i][1]:
            return contatos[i]
    else:
        return []
#todas funções testadas e funcionais até aq
