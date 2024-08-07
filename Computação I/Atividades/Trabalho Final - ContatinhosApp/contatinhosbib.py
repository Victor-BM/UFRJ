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
    if (type(contato[indice]) is str) and (nova_inf != ''):
        contato[indice] = nova_inf
        list.insert(contatos_geral, ind, contato)
        del contatos_geral[ind+1]
        return True
    elif (type(contato[indice]) is list) and  (nova_inf not in contato[indice]) and (nova_inf != ''):
        if '' in contato[indice]:
            del contato[indice][0]
        list.append(contato[indice], nova_inf)
        list.insert(contatos_geral, ind, contato)
        del contatos_geral[ind+1]
        return True
    else:
        return False
    
def excluir_telefone (contato, telefone):
    '''Função que permite excluir o telefone (ou qualquer múltipla informação) do contato
    list, string -> bool'''
    indice = list.index(contatos_geral, contato)
    ind = 1
    for i in contato:
        if telefone in i:
            ind = list.index(contato, i)#para múltiplas informações, ou seja, quando aglutina
    if type(contatos_geral[indice][ind]) is list:
        if telefone in contatos_geral[indice][ind]:
            list.remove(contatos_geral[indice][ind], telefone)
            if not contatos_geral[indice][ind]:
                list.append(contatos_geral[indice][ind], '')
            return True
    elif type(contatos_geral[indice][ind]) is str:
        if telefone == contatos_geral[indice][ind]:
            contatos_geral[indice][ind] = ''
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
        for g in [indice1, indice2]:
            if contatos_geral[g][1][0] == '':
                del contatos_geral[g][1][0]
        for i in range(len(contatos_geral[indice2][1])):
            if (contatos_geral[indice2][1][i] not in contatos_geral[indice1][1]):
                list.append(contatos_geral[indice1][1], contatos_geral[indice2][1][i])
        if not contatos_geral[indice1][1]:#para o caso de aglutinar dois contatos com números vazios
            list.append(contatos_geral[indice1][1], '')
        for j in range(2, 4):
            if (contatos_geral[indice1][j]) == '':
                contatos_geral[indice1][j] = contatos_geral[indice2][j]
        del contatos_geral[indice2]
