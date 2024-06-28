#Trabalho Final - ContatinhosApp - Parte 1 - Víctor BM
contatos_geral = []
def criar_contato (nome, telefone = '', email = '', instagram = ''):
    '''Função que permite criar contatos com apenas o nome obrigatório
    str, str, str, str -> list'''
    telefones = [telefone,]
    contato1 = [nome, telefones, email, instagram]
    return contato1

def atualizar_contato (contato, indice, nova_inf):
    '''Função que permite atualizar o contato adicionando uma nova informação pelo indice
    0 -> nome; 1 -> telefones; 2 -> email, 3 -> instagram
    list, int, str -> bool'''
    ind = list.index(contatos_geral, contato)
    if (indice == 0 or indice == 2 or indice == 3) and (nova_inf != ''):
        contato[indice] = nova_inf
        list.insert(contatos_geral, ind, contato)
        del contatos_geral[ind+1]
        return True
    elif indice == 1 and  (nova_inf not in contato[1]) and (nova_inf != ''):
        list.append(contato[1], nova_inf)
        if '' in contato[1]:
            del contato[1][0]
        list.insert(contatos_geral, ind, contato)
        del contatos_geral[ind+1]
        return True
    else:
        return False
    
def excluir_telefone (contato, telefone):
    '''Função que permite excluir o telefone do contato
    list, string -> bool'''
    indice = list.index(contatos_geral, contato)
    if type(contatos_geral[indice][1]) is list:
        if telefone in contatos_geral[indice][1]:
            list.remove(contatos_geral[indice][1], telefone)
            return True
    return False

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

def quem_ligou(ligacao):
    '''Função que retorna os dados de quem ligou
    str -> list'''
    for i in range(len(contatos_geral)):
        if type(contatos_geral[i][1]) is list:
            for j in range(len(contatos_geral[i][1])):
                if ligacao in contatos_geral[i][1][j]:
                    return contatos_geral[i]
        if ligacao in contatos_geral[i][1]:
            return contatos_geral[i]
    else:
        return []

def excluir_contato(contatos, indice):
    '''Função que exclui um contato por completo dado a lista de todos os
    contatos e o indíce do contato a ser excluído
    list, int -> none'''
    if 0 <= indice <= (len(contatos_geral) - 1):
        del contatos_geral[indice]

def aglutinador (contatos, indice1, indice2):
    '''Função que, dado dois contatos, algutina eles. No entanto, mantém as informações
    do primeiro e adiciona caso haja algo novo do segundo
    list, int, int -> none'''
    if (0 <= indice1 <= (len(contatos_geral) - 1)) and (0 <= indice2 <= (len(contatos_geral) - 1)) and (indice1 != indice2):
        if contatos_geral[indice1][1][0] == '':
            del contatos_geral[indice1][1][0]
        for i in range(len(contatos_geral[indice2][1])):
            if (contatos_geral[indice2][1][i] not in contatos_geral[indice1][1]):
                list.append(contatos_geral[indice1][1], contatos_geral[indice2][1][i])
        for j in range(2, 4):
            if (contatos_geral[indice1][j] != contatos_geral[indice2][j]) and (contatos_geral[indice2][j] != ''):
                contatos_geral[indice1][j] = [contatos_geral[indice1][j]]
                list.append(contatos_geral[indice1][j], contatos_geral[indice2][j])
                if contatos_geral[indice1][j][0] == '':
                    del contatos_geral[indice1][j][0]
        del contatos_geral[indice2]
