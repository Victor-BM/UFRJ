import numpy as np
import matplotlib.pyplot as plt
import sympy as sp

#CHATGPT

# Passo 1: Solicitar ao usuário para inserir uma função
func_input = input("Digite uma função de x (por exemplo, x**2 + 3*x + 5): ")

# Passo 2: Definir a variável simbólica
x = sp.symbols('x')

# Passo 3: Definir a função e calcular a derivada
func = sp.sympify(func_input)
derivada = sp.diff(func, x)

# Passo 4: Criar um intervalo para plotagem
x_vals = np.linspace(-10, 10, 400)  # valores de x de -10 a 10
func_vals = [func.evalf(subs={x: val}) for val in x_vals]  # valores da função original
derivada_vals = [derivada.evalf(subs={x: val}) for val in x_vals]  # valores da derivada

# Passo 5: Plotar as funções
plt.figure(figsize=(10, 6))
plt.plot(x_vals, func_vals, label=f'Função: {func}', color='blue')
plt.plot(x_vals, derivada_vals, label=f'Derivada: {derivada}', color='red')
plt.title('Função e sua Derivada')
plt.xlabel('x')
plt.ylabel('y')
plt.axhline(0, color='black', lw=0.5, ls='--')
plt.axvline(0, color='black', lw=0.5, ls='--')
plt.grid()
plt.legend()
plt.show()

