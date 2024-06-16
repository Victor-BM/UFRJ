#Quest1 - LabIdle 10 - Víctor BM
import random
def repetidos (valores):
    '''Função que conta a quantidade de séries
    repetidas em um dado
    list -> int'''
    i, count = 0, 0
    while i < len(valores):
        if i > 0 and (valores[i-1] == valores[i]):
            if i == 1:
                count += 1
            elif i > 1 and(valores[i-1] != valores[i-2]):
                count += 1
        i += 1
    return count

def main():
    jogadas = []
    tamanho = int(input('Quantas vezes o dado foi jogado? '))
    for j in range(tamanho):
        numero = int(input(f'Qual o valor da jogada {j + 1}? '))
        list.append(jogadas, numero)
    print(f'Número de séries de faces repetidas: {repetidos(jogadas)}')
    input()#Linha apenas para que seja possível rodar esse código no CMD do computador
main()