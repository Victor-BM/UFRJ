def gorjeta (conta):
    return (conta*0.15)
while (True):
    a = float(input("Qual o valor da conta? "))
    print (f'A gorjeta do garçom é de: {gorjeta(a)} reais')