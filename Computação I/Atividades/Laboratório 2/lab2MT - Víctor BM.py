#lab2MT - Víctor BM
import math

#Quest 1
def num_bombons (dinheiro, preco):
    '''Função para calcular quantos bombons Pedro pode comprar;
    int, int -> int'''
    return (dinheiro//preco)

#Quest 2
def carros (pessoas, capacidade = 5):
    '''Função para calcular quantidade de carros para transporte
    int, int -> int'''
    return math.ceil(pessoas/capacidade)

#Quest 3
def bolos (xicaras, ovos, leite):
    '''Função para calcular quantos bolos podem ser feitos
    int, int, int -> int'''
    a = xicaras//2
    b = ovos//3
    c = leite//5
    return min(a, b, c)
    
