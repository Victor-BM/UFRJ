import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def p_cuba ():
    # Dados da tabela (positivos e negativos)
    y = np.array([3, 6, 9, 12, 15, 18, 21, 24])      # ΔN
    x = np.array([710, 660, 600, 530, 460, 410, 350, 290])       # pcuba
    xerr = np.array([10, 10, 10, 10, 10, 10, 10, 10])      # incertezas pcuba

    # Modelo linear
    def linear(x, a, b):
        return a*x + b

    # Ajuste ponderado pelas incertezas
    popt, pcov = curve_fit(linear, x, y, sigma=xerr, absolute_sigma=True)
    a, b = popt
    da, db = np.sqrt(np.diag(pcov))

    print(f"Coeficiente Angular = {a:.2e} ± {da:.2e}")
    print(f"Interseção = {b:.2e} ± {db:.2e}")

    # Plot
    plt.errorbar(x, y, xerr=xerr, fmt='o', label='Dados')
    xx = np.linspace(290, 710, 100)
    plt.plot(xx, linear(xx, *popt), 'r-', label=f"Ajuste: y = {a:.2e}x + {b:.2e}")
    plt.xlabel("pcuba")
    plt.ylabel("ΔN")
    plt.legend(loc='upper right')
    plt.grid(True)
    
    plt.show()

    y_fit = linear(x, a, b)
    ss_res = np.sum((y - y_fit)**2)              # soma dos quadrados dos resíduos
    ss_tot = np.sum((y - np.mean(y))**2)         # soma total
    r2 = 1 - ss_res/ss_tot
    print(f"R² = {r2:.4f}")
    alpha = a*(-632.8*10**(-9))
    alpha = alpha/(2*55*10**(-3))
    print(f'α = {alpha} mmHg⁻¹')
    n_ar = 1 + alpha*760
    print(f'n_ar = {n_ar}')
    print(f'n_ar - n_vac = {n_ar - 1}')
p_cuba()
