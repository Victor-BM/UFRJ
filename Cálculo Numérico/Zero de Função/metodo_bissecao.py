import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

x = sp.symbols('x')
f_simbolica = x + sp.log(x, 10) #definir função
f_numerica = sp.lambdify(x, f_simbolica, 'numpy')

def secante(a, b, erro, arredondamento):
    xo = a
    x1 = b
    erro = erro
    i = 0
    arredondamento = arredondamento
    while i < 100:
        x_novo = (xo+x1)/2
        x_novo = np.round(x_novo, arredondamento)
        i += 1
        if f_numerica(xo)*f_numerica(x_novo) < 0:
            x1 = x_novo
            if abs(x_novo - xo) <= erro:
                print(f'raiz = {x_novo}\n{i} iterações')
                return
        else:
            xo = x_novo
            if abs(x_novo - x1) <= erro:
                print(f'raiz = {x_novo}\n{i} iterações')
                return
    print(f'Método da Bisseção após 100 iterações: raiz = {x_novo}')

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
    a = float(input('Qual a utilizar? '))
    b = float(input('Qual b utilizar? '))
    erro = float(input('Qual erro utilizar? '))
    arredondamento = int(input('Quantas casas decimais de arredondamento? '))
    k = (np.log(b-a) - np.log(erro))/np.log(2)
    print(f'k = {k}')
    secante(a, b, erro, arredondamento)
main()