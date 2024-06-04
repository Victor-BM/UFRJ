#LabIdle 9 - Víctor BM
#Q1
def mult_matriz_real(matriz, numero):
    '''Função que calcula a multiplicação de uma matriz por um real
    list, float -> list'''
    mat_res, x = [], 0
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[0])):
            x = matriz[i][j]
            list.append(linha, (x*numero))
        list.append(mat_res, linha)
    return mat_res

#Q2
def deu_match (afinidades):
    '''Função que determina afinidades mútuas
    dict -> list com tups dentro'''
    resposta = []
    pessoas = list(dict.items(afinidades))
    for pessoa1, curtidas in pessoas:
        for pessoa2 in curtidas:
            if (pessoa1 in dict.get(afinidades, pessoa2)) and (pessoa2, pessoa1) not in resposta:
                list.append(resposta, (pessoa1, pessoa2))
    return resposta

#Q3
contatos = []
def criar_contato (nome, telefone = '', email = '', instagram = ''):
    '''Função que permite criar contatos com apenas o nome obrigatório
    str, str, str, str -> list'''
    telefones = [telefone,]
    contato1 = [nome, telefones, email, instagram]
    list.append(contatos, contato1)
    return contatos

def atualizar_contato (contato, indice, nova_inf):
    '''Função que permite atualizar o contato adicionando uma nova informação pelo indice
    0 -> nome; 1 -> telefones; 2 -> email, 3 -> instagram
    list, str, int, str -> bool'''
    if indice == 0 or indice == 2 or indice == 3:
        list.remove(contatos, contato)
        contato[indice] = nova_inf
        list.append(contatos, contato)
        return True
    elif indice == 1 and (nova_inf != contato[1][0]):
        list.remove(contatos, contato)
        list.append(contato[1], nova_inf)
        list.append(contatos, contato)
        return True
    else:
        return False

def quem_ligou(ligacao):
    '''Função que retorna os dados de quem ligou
    str -> list'''
    for element in contatos:
        if ligacao in element[1]:
            return element
    else:
        return []
