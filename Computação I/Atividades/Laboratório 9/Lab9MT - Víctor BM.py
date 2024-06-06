#LabMT 9 - Víctor BM
#Q1
def eh_quadrada (matriz):
    '''Verifica se a matriz é quadrada
    list -> bool'''
    if len(matriz)== 0:
        return True
    elif len(matriz) == len(matriz[0]): 
        return True
    else:
        return False

#Q2
def conta_numero(numero, matriz):
    '''Conta a quantidade de vezes que um numero aparece na matriz de inteiros
    int, list -> int'''
    resposta = 0
    for i in range(len(matriz)):
        resposta += list.count(matriz[i], numero)
    return resposta

#Q3
def media_matriz(matriz):
    '''Faz a média dos elementos da matriz (podem ser int ou float) com
    duas casas de precisao
    list -> float'''
    total, media = 0, 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            total += matriz[i][j]
    media = total/(len(matriz)*len(matriz[i]))
    media = round(media, 2)
    return media

#Q4
def melhor_volta(corridas):
    '''Função que recebe uma matriz de 6 jogadores por 10 voltas
    e retorna o melhor competidor, sua melhor volta e o tempo dela
    list -> tup'''
    competidor, volta, tempo, melhor_tempo = 0, 0, 0, []
    for i in range (len(corridas)):
        list.append(melhor_tempo, min(corridas[i]))
    tempo = min(melhor_tempo)
    for j in range(len(corridas)):
        for k in range(len(corridas[i])):
            if corridas[j][k] == tempo:
                competidor = j + 1
                volta = k + 1
    return (competidor, tempo, volta)

#Q5
def busca (setor, infos):
    '''Retorna todos os funcionarios de determinado setor ao receber uma matriz
    cuja cada linha é: nome, registro, setor, telefone
    str, list -> list'''
    resposta = []
    for i in range(len(infos)):
        if setor in infos[i]:
            list.remove(infos[i], setor)
            list.append(resposta, infos[i])
    return resposta
        







    
