def dist (num1, num2, num3):
    t1 = num2/num1
    d2 = t1*num3
    return (d2)
while (True):
    a = float(input("Qual a velocidade do barco em m/s? "))
    b = float(input("Qual a largura do rio em metros? "))
    c = float(input("Qual a velocidade da correnteza em m/s? "))
    print (f'O barco foi arrastado por: {dist(a, b, c)} metros')