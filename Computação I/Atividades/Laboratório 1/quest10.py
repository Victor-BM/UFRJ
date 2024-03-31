def juros (num1, num2, num3):
    return (num1*(1+(num2*(num3/100))))
while (True):
    a = float(input("Informe o saldo inicial em reais: "))
    b = int(input("Qual o juros [Informe em naturais]? "))
    c = float(input("Quantos meses? "))
    print (f'O saldo final é de: {juros(a, b, c)} reais')