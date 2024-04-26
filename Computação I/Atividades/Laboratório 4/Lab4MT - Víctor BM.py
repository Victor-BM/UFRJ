#Lab4MT - Víctor BM

#Q1
def concatenacao (a, b):
    '''Função que concatena duas strings no formato abba
    str, str -> str'''
    return a + b + b + a

#Q2
def substitui (s, x, i):
    '''Função que recebe uma string, um caracter e um valor int entre 0 e o tamanho da string
    Assim, uma nova string é gerada substituindo o indice i por x
    str, str, int -> str'''
    return s[0:i] + x + s[i+1::]

#Q3
def hashtag (s):
    '''Função que insere uma hashtag no inicio, no meio e no final de uma string
    str -> str'''
    tamanho = len(s)
    return '#' + s[0:(tamanho//2)] + '#' + s[(tamanho//2)::] + '#'

#Q4
def filtra_pares (nums):
    '''Função que recebe uma tupla de 4 inteiros e retorna apenas os pares
    tupla(int, int, int, int) -> tupla (int, int, int, int)'''
    par = ()
    if nums[0]%2 == 0:
        par = par + (nums[0],)
    if nums[1]%2 == 0:
        par = par + (nums[1],)
    if nums[2]%2 == 0:
        par = par + (nums[2],)
    if nums[3]%2 == 0:
        par = par + (nums[3],)
    return par

#Q5
def colisao(ret1,ret2):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    x_inf_esq1, y_inf_esq1, x_sup_dir1, y_sup_dir1 = ret1
    x_inf_esq2, y_inf_esq2,  x_sup_dir2, y_sup_dir2 = ret2
    if (x_inf_esq1 <= x_sup_dir2) and (x_inf_esq2 <= x_sup_dir1) and (y_inf_esq1 <= y_sup_dir2) and (y_inf_esq2 <= y_sup_dir1):
        return True
    else:
        return False
