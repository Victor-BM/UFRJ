def calc (a, b, c):
    disc = (b**2)+(-4*a*c)
    x1 = (-b + (disc**(1/2)))/2*a
    x2 = (-b +- (disc**(1/2)))/2*a
    return (x1,x2)
while (True):
    num1 = float(input("Qual o número A? "))
    num2 = float(input("Qual o número B? "))
    num3 = float(input("Qual o número C? "))
    print (f'As raízes são: {calc(num1, num2, num3)}')