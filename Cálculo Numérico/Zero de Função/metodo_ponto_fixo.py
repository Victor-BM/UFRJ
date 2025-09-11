import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
f_simbolica = x - ((sp.cos(x))**2) #definir função
phi_simbolica = (sp.cos(x))**2
f_numerica = sp.lambdify(x, f_simbolica, 'numpy')
phi_numerica = sp.lambdify(x, phi_simbolica, 'numpy')

def ponto_fixo(xo, erro, arredondamento):
    x_velho = xo
    i = 0
    arredondamento = arredondamento
    while i < 100:
        x_novo = phi_numerica(x_velho)
        x_novo = np.round(x_novo, arredondamento)
        i += 1
        if abs(x_novo - x_velho) <= erro:
            print(f'raiz = {x_novo}\n{i} iterações')
            return
        x_velho = x_novo
    print(f'Método de Ponto Fixo após 100 iterações: raiz = {x_novo}')

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
    ponto_fixo(xo, erro, arredondamento)
main()