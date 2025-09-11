import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
f_simbolica = x**2 - 2 #definir função
f_numerica = sp.lambdify(x, f_simbolica, 'numpy')

def secante(xo, x1, erro, arredondamento):
    xo = xo
    x1 = x1
    erro = erro
    i = 0
    arredondamento = arredondamento
    while i < 100:
        x_novo = x1 - ((f_numerica(x1))*((x1 - xo)/(f_numerica(x1) - f_numerica(xo))))
        x_novo = np.round(x_novo, arredondamento)
        i += 1
        if abs(x_novo - x1) <= erro:
            print(f'raiz = {x_novo}\n{i} iterações')
            return
        xo = x1
        x1 = x_novo
    print(f'Método da Secante após 100 iterações: raiz = {x_novo}')

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
    x1 = float(input('Qual x1 utilizar? '))
    erro = float(input('Qual erro utilizar? '))
    arredondamento = int(input('Quantas casas decimais de arredondamento? '))
    secante(xo, x1, erro, arredondamento)
main()