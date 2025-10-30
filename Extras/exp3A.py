import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def malus ():
    # Dados da tabela (positivos e negativos)
    x = np.array([5, 10, 15, 20, 25, 30, 35, 40, 45, 50])      # N
    y = np.array([3, 5.5, 8, 11, 14, 16.5, 19.5, 22.5, 25, 28])       # Δl
    y = y*(10**(-5))
    y = y/20
    yerr = np.array([25, 25, 25, 25, 25, 25, 25, 25, 25, 25])      # incertezas Δl
    yerr = yerr*(10**(-8))

    # Modelo linear
    def linear(x, a, b):
        return a*x + b

    # Ajuste ponderado pelas incertezas
    popt, pcov = curve_fit(linear, x, y, sigma=yerr, absolute_sigma=True)
    a, b = popt
    da, db = np.sqrt(np.diag(pcov))

    print(f"Coeficiente Angular = {a:.2e} ± {da:.2e}")
    print(f"Interseção = {b:.2e} ± {db:.2e}")

    # Plot
    plt.errorbar(x, y, yerr=yerr, fmt='o', label='Dados')
    xx = np.linspace(5, 50, 100)
    plt.plot(xx, linear(xx, *popt), 'r-', label=f"Ajuste: y = {a:.2e}x + {b:.2e}")
    plt.xlabel("N")
    plt.ylabel("Δl")
    plt.legend(loc='upper left')
    plt.grid(True)
    
    plt.show()

    y_fit = linear(x, a, b)
    ss_res = np.sum((y - y_fit)**2)              # soma dos quadrados dos resíduos
    ss_tot = np.sum((y - np.mean(y))**2)         # soma total
    r2 = 1 - ss_res/ss_tot
    print(f"R² = {r2:.4f}")



malus()
