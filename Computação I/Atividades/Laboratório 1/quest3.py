import numpy as np
def area (r1, r2):
    a1 = r1*r1*np.pi
    a2 = r2*r2*np.pi
    a = a1 - a2
    return (a)
while (True):
    a = float(input("Qual o raio 1? "))
    b = float(input("Qual o raio 2? "))
    print (f'A área da coroa é: {area(a, b)}')