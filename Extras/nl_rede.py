import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def nl_rede ():
    # Dados da tabela (positivos e negativos)
    lambda_a = np.array([5791, 5770, 5461, 4916, 4358, 4078, 4047])      # lambda (Å)
    x = lambda_a * 1e-7 #lambda (mm)
    y = np.array([0.291, 0.290, 0.275, 0.248, 0.219, 0.208, 0.204])       # sen(theta_max)
    yerr = np.array([0.006, 0.006, 0.006, 0.006, 0.007, 0.007, 0.007])      # incertezas

    # Modelo linear
    def linear(x, a):
        return a*x

    # Ajuste ponderado pelas incertezas
    popt, pcov = curve_fit(linear, x, y, sigma=yerr, absolute_sigma=True)
    a = popt[0]
    da = np.sqrt(pcov[0, 0]) 

    # Plot
    plt.errorbar(x, y, yerr=yerr, fmt='o', label='Dados')
    xx = np.linspace(min(x)*0.9, max(x)*1.1, 100)
    plt.plot(xx, linear(xx, *popt), 'r-', label=f"Ajuste: sen θ_max = {a:.2e}λ ")
    plt.xlabel("λ (mm)")
    plt.ylabel("sen θ_max")
    plt.legend()
    plt.grid(True)
    plt.show()

    y_fit = linear(x, a)
    ss_res = np.sum((y - y_fit)**2)              # soma dos quadrados dos resíduos
    ss_tot = np.sum((y - np.mean(y))**2)         # soma total
    r2 = 1 - ss_res/ss_tot
    print(f"R² = {r2:.4f}")

    print(f"Nl (teórico) = 500 mm⁻¹ \nNl = {a:.2e} ± {da:.2e} mm⁻¹\n\n")

nl_rede()
