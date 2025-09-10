import numpy as np
import matplotlib.pyplot as plt


def fenda_200um ():
    # Dados fornecidos
    m_over_d = np.array([2500, -2500, 5000, -5000, 7500, -7500])  # m^-1
    sin_theta = np.array([1.6e-3, -1.8e-3, 3.4e-3, -3.4e-3, 5.0e-3, -5.0e-3])
    erro_sin = np.array([0.2e-3]*6)  # incerteza absoluta

    # Ajuste linear forçando a origem
    slope = np.sum(m_over_d * sin_theta) / np.sum(m_over_d**2)

    # Valores para a linha de ajuste
    xfit = np.linspace(min(m_over_d)*1.1, max(m_over_d)*1.1, 200)
    yfit = slope * xfit

    # Gráfico
    plt.figure(figsize=(6,4))
    plt.errorbar(m_over_d, sin_theta, yerr=erro_sin, fmt='o', color='orange',
             ecolor='black', capsize=3, label="Dados experimentais")
    plt.plot(xfit, yfit, 'b-', label=f"Ajuste linear (λ = {slope*1e9:.1f} nm)")

    plt.xlabel("m/d (m$^{-1}$)")
    plt.ylabel("sin(θ)")
    plt.title("Gráfico de sin(θ) × m/d (d' = 0.2mm)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    y_pred = slope * m_over_d  # valores previstos
    ss_res = np.sum((sin_theta - y_pred)**2)
    ss_tot = np.sum((sin_theta - np.mean(sin_theta))**2)
    r2 = 1 - ss_res/ss_tot
    print(f"R² = {r2:.4f}")

    return (f'λ = {slope*1e9:.1f} nm', f'δλ = {0.05*slope*1e9:.1f} nm')

def fenda_400um ():
    m_over_d = np.array([1666.67, -1666.67, 3333.33, -3333.33, 6666.67, -6666.67])  # m^-1
    sin_theta = np.array([1.2e-3, -1.2e-3, 2.3e-3, -2.3e-3, 4.4e-3, -4.4e-3])
    erro_sin = np.array([0.2e-3]*6)  # mesma incerteza para todos os pontos

    # Ajuste linear forçando a origem
    slope = np.sum(m_over_d * sin_theta) / np.sum(m_over_d**2)

    # Valores para a linha de ajuste
    xfit = np.linspace(min(m_over_d)*1.1, max(m_over_d)*1.1, 200)
    yfit = slope * xfit

    # Gráfico
    plt.figure(figsize=(6,4))
    plt.errorbar(m_over_d, sin_theta, yerr=erro_sin, fmt='o', color='orange',
             ecolor='black', capsize=3, label="Dados experimentais")
    plt.plot(xfit, yfit, 'b-', label=f"Ajuste linear (λ = {slope*1e9:.1f} nm)")

    plt.xlabel("m/d (m$^{-1}$)")
    plt.ylabel("sin(θ)")
    plt.title("Gráfico de sin(θ) × m/d (d' = 0.4mm)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    y_pred = slope * m_over_d  # valores previstos
    ss_res = np.sum((sin_theta - y_pred)**2)
    ss_tot = np.sum((sin_theta - np.mean(sin_theta))**2)
    r2 = 1 - ss_res/ss_tot
    print(f"R² = {r2:.4f}")

    return (f'λ = {slope*1e9:.1f} nm', f'δλ = {0.05*slope*1e9:.1f} nm')
def main():
    lambdas = [fenda_200um(), fenda_400um()]
    print('----------- Lambdas e Incertezas -----------')
    print(lambdas[0:2])
main()
