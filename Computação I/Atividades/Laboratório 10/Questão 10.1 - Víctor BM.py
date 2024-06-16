#Questão 1 - LabIdle 10 - Víctor BM
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
    while True:
        jogadas = []
        tamanho = int(input('Quantas vezes o dado foi jogado? '))
        for j in range(tamanho): #para transformar o input em uma lista
            numero = int(input(f'Qual o valor da jogada {j + 1}? '))
            list.append(jogadas, numero)
        print(f'Número de séries de faces repetidas: {repetidos(jogadas)}')
        repetidor = str(input('Você deseja usar a função novamente? [S ou N] ')).lower()
        if repetidor == 'n':
            break
main()