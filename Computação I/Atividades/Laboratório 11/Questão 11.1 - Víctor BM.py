#Questão 1 - LabIdle 11 - Víctor BM
import random as rand
def imprimidor(mat_user):
    '''Função própria para imprimir a matriz para o usuário
    list -> none'''
    print('\n')
    for i in range (4):
        print('       ' + f'{mat_user[i][0]}' + '  ' + f'{mat_user[i][1]}' + '  ' +  f'{mat_user[i][2]}' + '  ' + f'{mat_user[i][3]}' + '  ')
    print('\n')

def cria_matriz():
    '''Função que cria o corpo das matrizes utilizadas
    none -> list'''
    resposta = []
    for i in range(4):
        linha = []
        for j in range(4):
            list.append(linha, '*')
        list.append(resposta, linha)
    return resposta

def interface(memoria):
    '''Função que realiza a interface com o usuário e conta quantas jogadas foram necessárias
    list -> int'''
    print('Para jogar, passe uma lista da seguinte maneira -> [x, y]')
    print('Lembre-se, valores possíveis para x e y estão no intervalo fechado entre 0 e 3')
    mat_user = cria_matriz()
    jogadas, count, aux = 0, 0, []
    while True:
        imprimidor(mat_user)
        x1, y1 = eval(input('Escolha a primeira posição: '))
        while True:
            if (0 <= x1 <= 3) and (0 <= y1 <=3) and (mat_user[x1][y1] == '*'):
                break
            x1, y1 = eval(input('Posição inválida, escolha a primeira posição: '))
        mat_user[x1][y1] = memoria[x1][y1]
        imprimidor(mat_user)
        x2, y2 = eval(input('Escolha a segunda posição: '))
        while True:
            if (0 <= x2 <= 3) and (0 <= y2 <=3) and ((x2 != x1) or (y2 != y1)) and (mat_user[x2][y2] == '*'):
                break
            x2, y2 = eval(input('Posição inválida ou já escolhida, escolha a segunda posição: '))
        jogadas += 1
        mat_user[x2][y2] = memoria[x2][y2]
        imprimidor(mat_user)
        if mat_user[x1][y1] == mat_user[x2][y2]:
            print('Parabéns! Você acertou!')
        else:
            print('Você errou, tente novamente')
            mat_user[x1][y1] = '*'
            mat_user[x2][y2] = '*'
        count = 0
        for i in range(4):
            count += list.count(mat_user[i], '*')
        if count == 2:
            break
    for j in range(4):
        if '*' in mat_user[j]:
            list.append(aux, j)
            list.append(aux, list.index(mat_user[j], '*'))
    mat_user[aux[0]][aux[1]] = memoria[aux[0]][aux[1]]
    mat_user[aux[2]][aux[3]] = memoria[aux[2]][aux[3]]
    imprimidor(mat_user)
    return jogadas

def matriz_resposta():
    '''Função que cria a matriz resposta do jogo da memória
    none -> list'''
    memoria = cria_matriz()
    possibilidades = [1, 2, 3, 4, 5, 6, 7, 8]
    for i in range (4):
        for j in range (4):
            numero = rand.sample(possibilidades, 1)
            memoria[i][j] = numero[0]
            aparicoes = 0
            for k in range(4):
                aparicoes += list.count(memoria[k], numero[0])
            if aparicoes == 2:
                list.remove(possibilidades, numero[0])
    return (memoria)

def main():
    while True:
        print('   Jogo da memória 4x4   ')
        print(f'Parabéns! Você solucionou o jogo da memória em {interface(matriz_resposta())} jogadas')
        repetidor = str(input('Você deseja jogar novamente? [S ou N]: ')).lower()
        if repetidor == 'n':
            break
main()