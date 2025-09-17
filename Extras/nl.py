import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit


def n_forca_origem(): #testes




    # Dados da tabela (positivos e negativos)
    x = np.array([6.5e-4, 1.3e-3, -6.5e-4, -1.3e-3, 0])   # m*lambda (mm)
    y = np.array([0.337, 0.665, -0.340, -0.676, 0])       # sen(theta_max)
    yerr = np.array([0.003, 0.002, 0.003, 0.002, 0.00001])      # incertezas

    # Modelo linear
    def linear(x, a, b):
        return a*x + b

    # Ajuste ponderado pelas incertezas
    popt, pcov = curve_fit(linear, x, y, sigma=yerr, absolute_sigma=True)
    a, b = popt
    da, db = np.sqrt(np.diag(pcov))

    print(f"Nl = {a:.2e} ± {da:.2e} mm⁻¹")
    print(f"Interseção = {b:.2e} ± {db:.2e}")

    # Plot
    plt.errorbar(x, y, yerr=yerr, fmt='o', label='Dados')
    xx = np.linspace(min(x)*1.1, max(x)*1.1, 100)
    plt.plot(xx, linear(xx, *popt), 'r-', label=f"Ajuste: y = {a:.2e}x + {b:.2e}")
    plt.xlabel("mλ (mm)")
    plt.ylabel("sen θ_max")
    plt.legend()
    plt.grid(True)
    plt.show()

def nl_500 ():
    # Dados da tabela (positivos e negativos)
    x = np.array([6.5e-4, 1.3e-3, -6.5e-4, -1.3e-3, 0])   # m*lambda (mm)
    y = np.array([0.337, 0.665, -0.340, -0.676, 0])       # sen(theta_max)
    yerr = np.array([0.003, 0.002, 0.003, 0.002, 0.00001])      # incertezas

    # Modelo linear
    def linear(x, a):
        return a*x

    # Ajuste ponderado pelas incertezas
    popt, pcov = curve_fit(linear, x, y, sigma=yerr, absolute_sigma=True)
    a = popt[0]
    da = np.sqrt(pcov[0, 0]) 

    # Plot
    plt.errorbar(x, y, yerr=yerr, fmt='o', label='Dados')
    xx = np.linspace(min(x)*1.1, max(x)*1.1, 100)
    plt.plot(xx, linear(xx, *popt), 'r-', label=f"Ajuste: sen θ_max = {a:.2e}mλ ")
    plt.xlabel("mλ (mm)")
    plt.ylabel("sen θ_max")
    plt.legend()
    plt.grid(True)
    plt.show()

    y_fit = linear(x, a)
    ss_res = np.sum((y - y_fit)**2)              # soma dos quadrados dos resíduos
    ss_tot = np.sum((y - np.mean(y))**2)         # soma total
    r2 = 1 - ss_res/ss_tot
    print(f"R² = {r2:.4f}")

    return (f"Nl (teórico) = 500 mm⁻¹ \nNl = {a:.2e} ± {da:.2e} mm⁻¹\n\n")

def nl_1000 ():
    # Dados da tabela (positivos e negativos)
    x = np.array([6.5e-4, -6.5e-4, 0])      # m*lambda (mm)
    y = np.array([0.644, -0.672, 0])        # sen(theta_max)
    yerr = np.array([0.002, 0.002, 0.00001])      # incertezas

    # Modelo linear
    def linear(x, a):
        return a*x

    # Ajuste ponderado pelas incertezas
    popt, pcov = curve_fit(linear, x, y, sigma=yerr, absolute_sigma=True)
    a = popt[0]
    da = np.sqrt(pcov[0, 0]) 

    # Plot
    plt.errorbar(x, y, yerr=yerr, fmt='o', label='Dados')
    xx = np.linspace(min(x)*1.1, max(x)*1.1, 100)
    plt.plot(xx, linear(xx, *popt), 'r-', label=f"Ajuste: sen θ_max = {a:.2e}mλ ")
    plt.xlabel("mλ (mm)")
    plt.ylabel("sen θ_max")
    plt.legend()
    plt.grid(True)
    plt.show()

    y_fit = linear(x, a)
    ss_res = np.sum((y - y_fit)**2)              # soma dos quadrados dos resíduos
    ss_tot = np.sum((y - np.mean(y))**2)         # soma total
    r2 = 1 - ss_res/ss_tot
    print(f"R² = {r2:.4f}")

    return (f"Nl (teórico) = 1000 mm⁻¹ \nNl = {a:.2e} ± {da:.2e} mm⁻¹\n\n")
def main():
    N = [nl_500(), nl_1000()]
    print('----------- Nls e Incertezas -----------')
    print(N[0])
    print(N[1])
main()
