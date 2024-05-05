#Lab5MT - Víctor BM
#Q1
def concatenador(lista1, lista2):
    '''Função que gera uma terceira lista intercalando elementos da
    lista 1 e da lista 2
    list, list -> list'''
    a, b, c = lista1
    d, e, f = lista2
    lista3 = [a, d, b, e, c, f]
    return lista3

#Q2
def pontos_por_time (jogos):
    '''Função que recebe dados sobre jogos de ida e volta e calcula o numero de pontos
    de cada time. Exemplo:
    [['Cormengo','Flamínthians', [1, 0]], ['Flamínthians', 'Cormengo', [2, 2]]]
    list -> dict'''
    pontos_fla = 0
    pontos_cor = 0
    times = {'Flamínthians' : pontos_fla, 'Cormengo' : pontos_cor}
    if jogos[0][2][0] > jogos[0][2][1]:
        times[jogos[0][0]] += 3
    elif jogos[0][2][0] < jogos[0][2][1]:
        times[jogos[0][1]] += 3
    elif jogos[0][2][0] == jogos[0][2][1]:
        times[jogos[0][0]] += 1
        times[jogos[0][1]] += 1
    if jogos[1][2][0] > jogos[1][2][1]:
        times[jogos[1][0]] += 3
    elif jogos[1][2][0] < jogos[1][2][1]:
        times[jogos[1][1]] += 3
    elif jogos[1][2][0] == jogos[1][2][1]:
        times[jogos[1][0]] += 1
        times[jogos[1][1]] += 1
    return times
    
#Q3
def colchao(abc, h, l):
    '''Função que verifica se um colchao passa pela porta ou não a partir de suas medidas
    em ordem crescente e as medidas da porta
    list, int, int -> bool'''
    if ((abc[2] > h) and (abc[2] > l)) and ((abc[1] > h) and (abc[1] > l)):
        return False
    else:
        return True
