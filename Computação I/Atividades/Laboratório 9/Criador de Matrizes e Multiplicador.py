def matriz (n, m):
    matriz = []
    for i in range(n):
        linha = []
        for j in range(m):
            list.append(linha, 0)
        list.append(matriz, linha)
    return matriz

def mult_matrix(mat1, mat2):
    linha, mat_res = [], []
    x = 0
    for i in range(len(mat1)):
        linha = []
        for j in range(len(mat2[0])):
            x = 0
            for k in range(len(mat2)):
                x += mat1[i][k]*mat2[k][j]
            list.append(linha, x)
        list.append(mat_res, linha)
    return mat_res
