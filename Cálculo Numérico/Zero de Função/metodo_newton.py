import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
f_simbolica = sp.exp(-x)*(sp.log(x, 10) - (2/(x*sp.ln(10))) - ((x**(-2))/sp.ln(10))) #definir função
derivada_f_simbolica = sp.diff(f_simbolica, x)
f_numerica = sp.lambdify(x, f_simbolica, 'numpy')
derivada_f_numerica = sp.lambdify(x, derivada_f_simbolica, 'numpy')

def newton(xo, erro, arredondamento):
    x_velho = xo
    i = 0
    arredondamento = arredondamento
    while i < 100:
        x_novo = x_velho - (f_numerica(x_velho)/derivada_f_numerica(x_velho))
        x_novo = np.round(x_novo, arredondamento)
        i += 1
        if abs(x_novo - x_velho) <= erro:
            print(f'raiz = {x_novo}\n{i} iterações')
            return
        x_velho = x_novo
    print(f'Método de Newton após 100 iterações: raiz = {x_novo}')

def main():
    x_vals = np.linspace(0.1, 20, 400)
    y_vals = f_numerica(x_vals)

    plt.figure(figsize=(8,5))
    plt.axhline(0, color="black", linestyle="--", linewidth=1)
    plt.plot(x_vals, y_vals)
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid(True)
    plt.show()
    xo = float(input('Qual xo utilizar? '))
    erro = float(input('Qual erro utilizar? '))
    arredondamento = int(input('Quantas casas decimais de arredondamento? '))
    newton(xo, erro, arredondamento)
main()