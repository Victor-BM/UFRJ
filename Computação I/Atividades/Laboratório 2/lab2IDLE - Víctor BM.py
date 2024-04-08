#lab2IDLE - Víctor BM

import math #Para usos futuros

#Quest 1B
def media_3 (n1, n2, n3):
    '''Função que calcula a média de 3 números inteiros
    int, int, int -> float'''
    return ((n1+n2+n3)/3)

#Quest 1C
def diferenca_maior_media (n1, n2, n3):
    '''Função que calcula a diferença do maior número com a média de 3 números
    int, int, int-> float'''
    return (max (n1, n2, n3) - media_3(n1, n2, n3))

#Quest 1D
def soma_menor_media (n1, n2, n3):
    '''Função que calcula a soma do menor número com a média de 3 números
    int, int, int -> float'''
    return (min (n1, n2, n3) + media_3(n1, n2, n3))

#Quest 2A
def discriminante (a, b, c):
    '''Calcula a discriminante de um polinômio de segundo grau
    float, float, float -> float'''
    return ((b**2) + (-4*a*c))

#Quest 2B
def primeira_raiz (a, b, c):
    '''Calcula a primeira raiz real de um polinômio de segundo grau
    float, float, float -> float'''
    return ((-b + ((discriminante (a, b, c))**(1/2)))/(2*a))
    
#Quest 2C
def segunda_raiz (a, b, c):
    '''Calcula a segunda raiz real de um polinômio de segundo grau
    float, float, float -> float'''
    return ((-b - ((discriminante (a, b, c))**(1/2)))/(2*a))

#Quest 3B
def termos_pa (a1, an, r):
    '''Função para calcular números de termos de uma progressão aritmética
    float, float, float -> int'''
    return (((an - a1)/r) + 1)

#Quest 3C
def soma_pa (a1, an, r):
    '''Função para calcular a soma de uma progressão aritmética
    float, float, float -> int'''
    return (((a1 + an)*(termos_pa (a1, an, r)))/2)

#Quest 4A
def distancia (xa, ya, xb, yb):
    '''Função para calcular a distancia entre dois pontos
    float, float, float, float -> float'''
    p = [xa, ya]
    q = [xb, yb]
    return (math.dist(p,q))

#Quest 4B
def perimetro_tri_reto (a, b):
    '''Função que calcula o perímetro de um triângulo retângulo dados os seus catetos
    float, float -> float'''
    h = math.sqrt((a**2) + (b**2))
    return a+b+h

#Quest 4C
def soma_sen_cos (angulo):
    '''Função que calcula a soma do quadrado do seno com a soma do quadrado do cosseno
    O valor de entrada do ângulo é feito em radianos
    float -> float'''
    return (math.sin(angulo)**2 + math.cos (angulo)**2)

#Quest 5
def setor_circular (raio, angulo = 2*math.pi):
    '''Função que calcula o setor circular com base no raio e no ângulo (se for dado)
    O valor de entrada do ângulo é feito em radianos
    float, float -> float'''
    (angulo/(2*math.pi))*math.pi*(raio**2)
    return ((angulo/(2*math.pi))*math.pi*(raio**2))
    










    
