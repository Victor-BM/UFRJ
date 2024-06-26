#Trabalho Final - ContatinhosApp - Víctor BM

def criar_contato (nome, telefone = '', email = '', instagram = ''):
    '''Função que permite criar contatos com apenas o nome obrigatório
    str, str, str, str -> list'''
    contatos_todos = []
    telefones = [telefone,]
    contato1 = [nome, telefones, email, instagram]
    list.append(contatos_todos, contato1)
    return contatos_todos

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
    
def excluir_telefone (contato, telefone):
    '''Função que permite excluir o telefone do contato
    list, string -> bool'''
    if telefone in contato[1]:
        list.remove(contato[1], telefone)
        return True
    else:
        return False

def buscar_contato (contatos, nome):
    '''Função que busca um contato em uma lista de contatos
    list, str -> list'''
    i = 0
    resposta = []
    nome = nome.lower()
    novo_contato = []
    while i<(len(contatos)):
        nome_contato = contatos[i][0]
        nome_contato = nome_contato.lower()
        if nome in nome_contato:
            resposta.append(contatos[i])
        i += 1
    return resposta

def quem_ligou(ligacao):
    '''Função que retorna os dados de quem ligou
    str -> list'''
    for element in contatos:
        if ligacao in element[1]:
            return element
    else:
        return []

def main():
    contatos = []
    contatos += criar_contato(cucucucucuc)