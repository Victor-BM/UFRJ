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

