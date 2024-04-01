def media (num1, num2, p1, p2):
    return (((num1*p1)+(num2*p2))/(p1+p2))
while (True):
    a = float(input("Qual o número 1? "))
    peso1 = float(input("Qual o peso 1? "))
    b = float(input("Qual o número 2? "))
    peso2 = float(input("Qual o peso 2? "))
    print (f'A média é ponderada: {media(a, b, peso1, peso2)}')