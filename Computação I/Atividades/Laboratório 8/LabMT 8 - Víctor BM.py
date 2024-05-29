#LabMT 8 - Víctor BM
#Q1
def freq_palavras (frases):
    '''Retorna um diicionario com as palavras e quantas vezes elas aparecem
    str -> dict'''
    resposta = {}
    palavras = str.split(frases)
    for i in range(len(palavras)):
        if palavras[i] in resposta:
            resposta[palavras[i]] += 1
        else:
            resposta[palavras[i]] = 1
    return resposta

#Q2
def total (compras, produtos):
    '''Função que calcula o valor total de uma compra
    list, dict -> float'''
    divida = 0
    for i in range(len(compras)):
        divida += produtos[compras[i]]
        divida = round (divida, 2)
    return divida

#Q3
def lingua_p (frase):
    '''Função que traduz uma frase pra lingua do p
    str -> str'''
    frase = str.lower(frase)
    nova_frase = ''
    vogais = 'âaáêeéiíôoóuúãõ'
    for i in frase:
        if i in vogais:
            nova_frase = nova_frase + i + 'p' + i
        else:
            nova_frase += i
    return nova_frase

#Q4
def qtd_divisores(numero):
    '''Função que conta quantos divisores cada numero possui
    int -> int'''
    contador = 0
    for i in range(1, numero + 1):
        if numero%i == 0:
            contador += 1
    return contador

#Q5
def primo(numero):
    '''Verifica se um numero é primo ou não
    int -> bool'''
    contador = 0
    if numero == 2:
        return True
    else:
        for i in range(2, (int(numero/2) + 1)):
            if numero%i == 0:
                contador += 1
        if contador != 0:
            return False
        else:
            return True
