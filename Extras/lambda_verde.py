import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def lambda_verde():

    # Dados da tabela (positivos e negativos)
    Nl = 504
    Nl_err = 4.76

    x_mm = np.array([-2, -1,0, 1, 2])*Nl
    x_err_mm = np.array([2, 1, 0.0001, 1, 2])*Nl_err # m*Nl (1/mm)

    x = x_mm / (1e7) # m*Nl (1/Å)
    xerr = x_err_mm / (1e7) #incerteza
    y = np.array([-0.469, -0.274, 0, 0.276, 0.558])       # sen(theta_max)
    yerr = np.array([0.007, 0.008, 0.0001, 0.008, 0.007])     # incertezas

    # Modelo linear
    def linear(x, a, b):
        return a*x + b

    # Ajuste ponderado pelas incertezas
    popt, pcov = curve_fit(linear, x, y, sigma=yerr, absolute_sigma=True)
    a, b = popt
    da, db = np.sqrt(np.diag(pcov))


    # Plot
    plt.errorbar(x, y, yerr=yerr, xerr=xerr, fmt='o', label='Dados')
    xx = np.linspace(min(x)*1.1, max(x)*1.1, 100)
    plt.plot(xx, linear(xx, *popt), 'r-', label=f"Ajuste: sen θ_max = {a:.2e}mNl + {b:.2e}")
    plt.xlabel("mNl (1/Å)")
    plt.ylabel("sen θ_max")
    plt.legend()
    plt.grid(True)
    plt.show()

    y_fit = linear(x, a, b)
    ss_res = np.sum((y - y_fit)**2)              # soma dos quadrados dos resíduos
    ss_tot = np.sum((y - np.mean(y))**2)         # soma total
    r2 = 1 - ss_res/ss_tot
    print(f"R² = {r2:.4f}")

    print(f"λ = {a:.2e} ± {da:.2e} Å")
    print(f"Interseção = {b:.2e} ± {db:.2e}")

lambda_verde()