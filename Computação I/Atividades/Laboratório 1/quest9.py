def gorjeta (conta, porc):
    return (conta*(porc/100))
while (True):
    a = float(input("Qual o valor da conta em reais? "))
    b = int(input("Qual a porcentagem da gorjeta [Informe em naturais]? "))
    print (f'A gorjeta do garçom é de: {gorjeta(a, b)} reais')