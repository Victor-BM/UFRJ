#LabIDLE 8 - Víctor BM
import math
#Q1
def aparicoes (iteravel, elem):
    '''Função que calcula a quantidade de vezes que elem aparece em iterável
    str/tup/list, str/tup/list/float -> int'''
    contador = 0
    for i in iteravel:
        if i == elem:
            contador += 1
    return contador

#Q2
def aparicoes_limitada (iteravel, elem, ini, fim):
    '''Função que calcula a quantidade de vezes que elem aparece em iterável limitado por indices positivos
    ini(inclusive) e fim(exclusive)
    str/tup/list, str/tup/list/float, int, int -> int'''
    contador = 0
    if (fim <= len(iteravel) - 1) and (ini <= len(iteravel) - 1):
        for i in range(ini, fim):
            if iteravel[i] == elem:
                contador += 1
    else:
        contador = aparicoes(iteravel, elem)
    return contador

#Q3
def atualiza_mascara(secreta, revelado, letra):
    '''Função que atualiza a mascara de uma forca
    por exemplo: carta, ['-', 'a', '-', '-', 'a'], t -> ['-', 'a', '-', 't', 'a']
    str, list, str -> list'''
    for i in range(len(secreta)):
        if letra == secreta[i]:
            revelado[i] = letra
    return revelado

#Q4
#a
def somatorio (termo):
    '''Função que faz  somatorio ((-1)**n)/(2n+1) de 0 até o termo
    int -> float'''
    soma = 0
    for i in range(termo+1):
        soma += ((-1)**i)/((2*i) + 1)
    return soma
#b
def diferenca_serie():
    '''Função que calcula a soma da serie ate que: |soma - (pi/4)| < 0.01 e também calcula o numero de termos necessario para isso
    -> tup'''
    soma = 0
    termo = 0
    while (True):
        soma = somatorio(termo)
        x = soma - (math.pi/4)
        if math.fabs(x) < 0.01:
            return (soma, termo)
        termo += 1
        
