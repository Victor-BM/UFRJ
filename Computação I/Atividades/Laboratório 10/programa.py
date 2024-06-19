#Questão 2 - LabIdle 10 - Víctor BM
def area_trapezio(a, b, c):
    '''Função que calcula a área de um trapézio
    int, int, int -> float'''
    area = ((a+b)*c)/2
    return area

def quadrados(a, b, c):
    '''Função que calcula o quadrado de cada variável
    int, int, int -> tup'''
    return (a*a, b*b, c*c)

def media_aritmetica(a, b, c):
    '''Função que calcula e média de 3 variáveis
    int, int, int -> float'''
    return ((a + b + c)/3)

def somador(a, b, c):
    '''Função que calcula a soma da primeira variável (inclusive) até a segunda variável (inclusive)
    usando a terceira variável como iterador
    int, int, int -> float'''
    soma = 0
    for i in range(a, b+1, c):
        soma += i
    return soma

def main():
    while True:
        while True:
            print('-|- Calculadora multifuncional com 3 variáveis -|-\nInsira 1 para calcular a área de um trapézio')
            print('Insira 2 para calcular o quadrado de cada variável\nInsira 3 para calcular a média aritmética entre as 3 variáveis')
            print('Insira 4 para calcular a soma da primeira variável (inclusive) até a segunda varíavel (inclusive), usando a terceira variável como iterador')
            i = int(input('Qual função você deseja utilizar? '))
            print('Dê as variáveis em inteiros, com a primeira variável menor que a segunda variável')
            if 1 <= i <= 4:
                break
            else:
                print('\n\nERRO. Função inválida! Existem as funções 1, 2, 3 e 4\n\n')
        a = int(input(f'Qual o valor da variável 1? '))
        while True:
            b = int(input(f'Qual o valor da variável 2? '))
            if a < b:
                break
            print('\n\nERRO. A primeira variável precisa ser menor que a segunda variável!\n\n')
        c = int(input(f'Qual o valor da variável 3? '))
        if i == 1:
            print(f'Variável 1: {a}\nVariável 2: {b}\nVariável 3: {c}')
            print(f'Área do trapézio: {area_trapezio(a, b, c)}')
        elif i == 2:
            print(f'Variável 1: {a}\nVariável 2: {b}\nVariável 3: {c}')
            print(f'Quadrado de cada variável, respectivamente: {quadrados(a, b, c)}')
        elif i == 3:
            print(f'Variável 1: {a}\nVariável 2: {b}\nVariável 3: {c}')
            print(f'Média aritmética: {media_aritmetica(a, b, c)}')
        else:
            print(f'Variável 1: {a}\nVariável 2: {b}\nVariável 3: {c}')
            print(f'Soma da primeira variável (inclusive) até a segunda variável (inclusive): {somador(a, b, c)}')
        repetidor = str(input('Você deseja usar a função novamente? [S ou N] ')).lower()
        if repetidor == 'n':
            break
main()