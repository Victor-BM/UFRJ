#Lab3IDLE - Víctor BM

#Q1
def absoluto (numero):
    '''Função que calcula o absoluto de um número
    float -> float'''
    if numero < 0:
        return numero*(-1)
    else:
        return numero

#Q2
def quantidade_raizes (a, b, c):
    '''Função que calcula a quantidade de raízes de uma equação do segundo grau
    float, float, float -> string'''
    discriminante = (b**2) + (-4*a*c)
    if discriminante > 0:
        return 'Duas raízes reais'
    elif discriminante < 0:
        return 'Nenhuma raiz real'
    else:
        return 'Uma raiz real'

#Q3
def repetidor (texto, numero_repet):
    '''Função que faz um texto se repetir
    string, int -> string'''
    return texto*numero_repet

#Q4
def data (dia, mes, ano):
    '''Função que retorna a data em dia/mes/ano
    string, string, string -> string'''
    return str(dia) + '/' + str(mes) + '/' + str(ano)

#Q5
def diferentes_funções (numero):
    '''Função que retorna uma diferente função matemática de acordo com o valor de entrada
    float -> string'''
    if numero < 0:
        return 0
    elif (numero >= 0) and (numero <= 2):
        return x
    elif (numero > 2) and (numero <= 3.5):
        return 2
    elif (numero > 3.5) and (numero <= 5):
        return 3
    else:
        return ((x**2) - (10*x) + 28))

#Q6 - a
def inss (salario_bruto):
    '''Função que calcula o desconto do imposto INSS
    float -> float'''
    if (salario_bruto <= 2000):
        return (salario_bruto*0.06)
    elif (salario_bruto <= 3000):
        return (salario_bruto*0.08)
    else:
        return (salario_bruto*0.1)

#Q6 - b
def imposto_renda (salario_bruto):
    '''Função que calcula o desconto do imposto de renda
    float -> float'''
    if (salario_bruto <= 2500):
        return (salario_bruto*0.11)
    elif (salario_bruto <= 5000):
        return (salario_bruto*0.15)
    else:
        return (salario_bruto*0.22)
    
#Q6 - c
def salario_liquido (salario_bruto):
    '''Função que calcula o salário líquido à partir do salário bruto
    e dos descontos do INSS e do imposto de renda
    float -> float'''
    return (salario_bruto - (inss(salario_bruto)) - (imposto_renda(salario_bruto)))
