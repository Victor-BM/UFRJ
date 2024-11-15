def dividir (numerador, denominador):
    try:
        resultado = numerador/denominador
    except ZeroDivisionError:
        print('Erro: Não é possível dividir por zero')
    else:
        print(resultado)

def potencia (numero, indice):
    try:
        resultado = numero**indice
    except TypeError:
        print('Erro: Ambos os argumentos devem ser números')

dividir(10, 0)
potencia('abc', 2)