#LabIdle 7 - Víctor BM
import random

#Q1
def dados ():
    '''Função que conta quantas vezes os dados foram jogados até que se caia um
    resultado igual em dois dados
    -> int'''
    count = 0
    d1 = 1
    d2 = 2
    while (d1 != d2):
        d1 = random.randint(1, 6)
        d2 = random.randint(1, 6)
        count += 1
    return count

#Q2
#A
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
