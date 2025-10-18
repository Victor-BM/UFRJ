import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def malus ():
    # Dados da tabela (positivos e negativos)
    x = np.array([1.000, 0.970, 0.883, 0.750, 0.587, 0.413, 0.250, 0.117, 0.030, 0.000, 0.030])      # cos²(θ1  - θ01)
    y = np.array([0.58, 0.58, 0.56, 0.53, 0.50, 0.46, 0.43, 0.40, 0.39, 0.37, 0.38])       # I1
    yerr = np.array([0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14, 0.14])      # incertezas I1

    # Modelo linear
    def linear(x, a, b):
        return a*x + b

    # Ajuste ponderado pelas incertezas
    popt, pcov = curve_fit(linear, x, y, sigma=yerr, absolute_sigma=True)
    a, b = popt
    da, db = np.sqrt(np.diag(pcov))

    print(f"I1_máx = {a:.2e} ± {da:.2e}")
    print(f"Interseção = {b:.2e} ± {db:.2e}")

    # Plot
    plt.errorbar(x, y, yerr=yerr, fmt='o', label='Dados')
    xx = np.linspace(0, 1, 100)
    plt.plot(xx, linear(xx, *popt), 'r-', label=f"Ajuste: y = {a:.2e}x + {b:.2e}")
    plt.xlabel("cos²(θ1  - θ01)")
    plt.ylabel("I1")
    plt.legend(loc='upper left')
    plt.grid(True)
    
    plt.show()

    y_fit = linear(x, a, b)
    ss_res = np.sum((y - y_fit)**2)              # soma dos quadrados dos resíduos
    ss_tot = np.sum((y - np.mean(y))**2)         # soma total
    r2 = 1 - ss_res/ss_tot
    print(f"R² = {r2:.4f}")



malus()
