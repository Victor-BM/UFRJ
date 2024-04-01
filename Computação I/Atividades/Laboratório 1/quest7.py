def pg (num1, num2):
    infini = (1/(1-num2))
    fini = ((num2**num1) - 1)/(num2 -1)
    return (infini - fini)
while (True):
    n = float(input("Defina N: "))
    q = float(input("De um Q racional maior ou igual a 0 e menor que 1: "))
    if q >= 0 and q<1:
        print (f'A diferença entre a soma infinita e a soma dos N primeiros termos é:: {pg(n, q)}')
    