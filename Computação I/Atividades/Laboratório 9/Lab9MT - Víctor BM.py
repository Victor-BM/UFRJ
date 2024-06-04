#LabMT 9 - Víctor BM
#Q1
def eh_quadrada (matriz):
    '''Verifica se a matriz é quadrada
    list -> bool'''
    if len(matriz) == len(matriz[0]):
        return True
    else:
        return False
