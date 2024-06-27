#Trabalho Final - ContatinhosApp - Parte 1 - Víctor BM
contatos_geral = []
def criar_contato (nome, telefone = '', email = '', instagram = ''):
    '''Função que permite criar contatos com apenas o nome obrigatório
    str, str, str, str -> list'''
    telefones = [telefone,]
    contato1 = [nome, telefones, email, instagram]
    list.append(contatos_geral, contato1)
    return contatos_geral

def atualizar_contato (contato, indice, nova_inf):
    '''Função que permite atualizar o contato adicionando uma nova informação pelo indice
    0 -> nome; 1 -> telefones; 2 -> email, 3 -> instagram
    list, int, str -> bool'''
    ind = list.index(contatos_geral, contato)
    if indice == 0 or indice == 2 or indice == 3:
        contato[indice] = nova_inf
        list.insert(contatos_geral, ind, contato)
        del contatos_geral[ind+1]
        return True
    elif indice == 1 and (nova_inf != contato[1]) and not(type(contato[1]) is list):
        contato[1] = [contato[1]]
        list.append(contato[1], nova_inf)
        list.insert(contatos_geral, ind, contato)
        del contatos_geral[ind+1]
        return True
    elif indice == 1 and (type(contato[1]) is list) and  (nova_inf not in contato[1]):
        list.append(contato[1], nova_inf)
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
#todas funções testadas e funcionais até aq ------> mas talvez a atualizar contato tenha q ser modificada
