import pandas as pd
import numpy as np
frequencia = [2000, 3000, 5000, 7000, 8000, 9733.6, 11000, 12000, 14000, 17000, 20000]
t = [119, 76.6, 41.6, 23.4, 15.0, -0.2, -8.0, -10.4, -11.7, -11.2, -9.9] #microssegundos
delta_t = [2, 0.8, 0.4, 0.6, 0.9, 0.2, 0.2, 0.6, 0.4, 0.3, 0.2]
R = 556
L = 24.0*(10**(-3))
C = 11.14*(10**(-9))
logs, phi, delta_phi, theta = [], [], [], []

def calcula_delta_phi(indice):
    return (np.absolute(2*np.pi*frequencia[indice]*delta_t[indice]*(10**(-6))))

def cria_tabela():
    for i in range(11):
        logs.append(np.log10(frequencia[i]))
        phi.append(2*np.pi*frequencia[i]*t[i]*(10**(-6)))
        delta_phi.append((calcula_delta_phi(i)))
        theta_calc = np.arctan(((1 - (4 * np.pi**2 * frequencia[i]**2 * L * C))) / (2 * np.pi * frequencia[i] * R * C))
        theta.append(theta_calc)

    df = pd.DataFrame({
        'Logs': logs,
        'Phi [rad]': phi,
        'Delta Phi [rad]': delta_phi,
        'Phi - N [rad]': theta
    })
    df.to_csv('tabela8.csv', index = False)

cria_tabela()
