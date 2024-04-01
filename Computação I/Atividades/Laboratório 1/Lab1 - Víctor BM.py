'''Laboratório 1 - Víctor BM'''

def area_ret (l1, l2):
    '''Função para calcular a área de um retângulo'''
    return (l1*l2)
def area_cubo (c1):
    '''Função para calcular a área de um cubo'''
    return (c1*c1*6)
def coroa (r1, r2):
    '''Função para calcular a área de uma coroa circular'''
    return ((r1*r1*3.14) - (r2*r2*3.14))
def media_simples (num1, num2):
    '''Função para calcular uma média simples de dois números'''
    return ((num1+num2)/2)
def calculadora_2grau (a, b, c, x):
    '''Função para calcular as raízes de uma equação do 2º grau'''
    y = a*(x**2) + b*x + c
    return (y)
def media_pond (n1, n2, p1, p2):
    '''Função para calcular a média pondrada de dois números'''
    return (((n1*p1)+(n2*p2))/(p1+p2))
def pg (n, q):
    '''Função para calcular a diferença entre as somas de uma PG de um Q racional maior ou igual a 0 e menor que 1'''
    infinito = (1/(1-q))
    finito = ((q**n) - 1)/(q -1)
    return (infinito - finito)
def gorjeta_simples (conta):
    '''Função para calcular a gorjeta de um garçom com taxa fixa'''
    return (conta*0.15)
def gorjeta_var (cont, porc):
    '''Função para calcular a gorjeta de um garçom com taxa variável. Dê a porcentagem no formato de inteiros'''
    return (cont*(porc/100))
def juros (saldo, juro, meses):
    '''Função para calcular juros simples. Dê todos os valores em inteiros'''
    return (saldo*(1+(meses*(juro/100))))
def arraste (barco, largura, cor):
    '''Função para calcular o arraste de um barco'''
    t1 = largura/barco
    d2 = t1*cor
    return (d2)
                  
