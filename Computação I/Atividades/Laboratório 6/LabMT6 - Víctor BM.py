#LabMT6 - Víctor BM
#Q1
def quant_palavras(frase):
    '''Função que retorna o numero de palavras de uma frase
    string -> int'''
    palavras = str.split(frase)
    return len(palavras)

#Q2
def conta_frases(texto):
    '''Função que retorna o numero de frases em um texto
    string -> int'''
    a = str.count(texto, '.')#para 3 pontos, conta 3 vezes
    b = str.count(texto, '!')
    c = str.count(texto, '?')
    d = str.count(texto, '...')#para 3 pontos, conta 1 vez
    return (a + b + c - (2*d))

#Q3
def retira_pontuacao(frase):
    '''Função que retira pontuação
    str -> str'''
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    return frase

#Q4
def inverte (frase):
    '''Função que retorna a frase com as palavraas na ordem inversa, sem maiusculas e sem potnuação
    str -> str'''
    frase = str.lower(frase)
    frase = str.replace(frase, '-', ' ')
    frase = str.replace(frase, ',', ' ')
    frase = str.replace(frase, ':', ' ')
    frase = str.replace(frase, ';', ' ')
    frase = str.replace(frase, '.', ' ')
    frase = str.replace(frase, '!', ' ')
    frase = str.replace(frase, '?', ' ')
    palavras = str.split(frase)
    palavras = palavras[::-1]
    palavras = str.join(' ', palavras)
    return palavras

#Q5
def insere(lista_numero, n):
    '''Função que ordena uma lista em crescente de inteiros, insere n na posicao correta paa continuar em ordem
    list -> list'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero

#Q6
def maiores (lista_numero, n):
    '''Função que retorna os numeros maiores que n em ordem crescente
    list -> list'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    x = list.index(lista_numero, n)
    return lista_numero[x+1::]
    
#Q7
def acima_da_media (notas):
    '''Função que retorna as notas que ficaram acima de média
    list -> list'''
    media = (sum(notas))/(len(notas))
    list.append(notas, media)
    list.sort(notas)
    x = 
