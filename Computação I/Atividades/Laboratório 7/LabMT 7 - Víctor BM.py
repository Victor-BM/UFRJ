#LabMT 7 - Víctor BM
#Q1
def filtraMultiplos (numeros, n):
    '''Função que filtra os numeros multiplos de n
    list, int -> list'''
    i = 0
    multiplo = []
    while i < (len(numeros)):
        if numeros[i]%n == 0:
            list.append(multiplo, numeros[i])
        i += 1
    return multiplo

#Q2
def uppCons (frase):
    '''Função que faz as consoantes ficarem em maiusculo
    str -> str'''
    nova_frase = ''
    i = 0
    consoantes = 'BbCcDdFfGgHhJjKkLlMmNnPpQqRrSsTtVvXxYyZzÇç'
    while i < (len(frase)):
        caracter = frase[i]
        if caracter in consoantes:
            caracter = caracter.upper()
        nova_frase += caracter 
        i += 1
    return nova_frase

#Q3
def posLetra (frase, letra, ocorrencia):
    '''Função que recebe a frase, letra e a ocorrencia e retorna o indice da ocorrencia, se a ocorrencia n existe
    a resposta é -1.
    str, str, int -> int'''
    i = 0
    count = 0
    while i< (len(frase)):
        if letra == frase[i]:
            count += 1
        if count == ocorrencia:
            return i
        i += 1
    return -1

#Q4
def repetidos(numeros):
    '''Função que retorna o numero de vezes que elemento da lista é igual ao anterior
    list -> int'''
    i = 1
    count = 0
    while i<(len(numeros)):
             if (numeros[i-1] == numeros[i]):
                 count += 1
             i += 1
    return count

#Q5
def fatorial(numero):
    '''Calcula o fatorial do numero
    int -> float'''
    i = 1
    fact = 1
    while i <= numero:
        fact *= i
        i += 1
    return fact

#Q6
def faltante (pecas):
    '''Retorna o primeiro numero que nao pertence  peças em ordem crescente
    list -> int'''
    list.sort(pecas)
    i = 1
    while i <= (pecas[-1] + 1):
        if i not in pecas:
            return i
        i += 1
        
