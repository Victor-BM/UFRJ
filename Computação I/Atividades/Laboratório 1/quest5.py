def calc (a, b, c, x):
    disc = (b**2)+(-4*a*c)
    y = a*(x**2) + b*x + c
    return (y)
while (True):
    num1 = float(input("Qual o número A? "))
    num2 = float(input("Qual o número B? "))
    num3 = float(input("Qual o número C? "))
    xis = float(input("Qual o número X? "))
    print (f'O valor de f(x) para quando X = {xis} é: {calc(num1, num2, num3, xis)}')