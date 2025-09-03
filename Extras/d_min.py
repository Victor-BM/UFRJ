import numpy as np
import matplotlib.pyplot as plt

# Ângulo do prisma (em graus → rad)
A_deg = 60       # se quiser usar o valor real: 119 + 48.5/60
A = np.deg2rad(A_deg)

# Dados experimentais: (nome, cor, λ (nm), D_min em graus)
data = [
    ("Amarelo 1", "gold",      5791, 50 + 12.5/60),
    ("Amarelo 2", "goldenrod", 5770, 50 + 12.5/60),
    ("Verde",     "green",     None, 50 + 11.5/60),  # sem λ
    ("Verde-azul","teal",      4916, 50 + 12.5/60),
    ("Azul-anil", "blue",      4358, 49 + 14/60),
    ("Violeta 1", "purple",    4078, 49 + 35/60),
    ("Violeta 2", "indigo",    4047, 49 + 52/60),
]
delta = 0.5/60
delta = np.deg2rad(delta)
print(delta)
# Função do desvio angular
def desvio(i, n):
    r1 = np.arcsin(np.sin(i)/n)
    r2 = A - r1
    i2p = np.arcsin(n*np.sin(r2))
    return i + i2p - A

plt.figure(figsize=(8,6))

# Loop pelas cores
for nome, cor, lam, Dmin_deg in data:
    Dmin = np.deg2rad(Dmin_deg)
    n = np.sin((A + Dmin)/2) / np.sin(A/2)
    delta_n = abs((np.cos((Dmin + A)/2))/(2*np.sin(A/2))*delta)


    # Ângulo de incidência no mínimo
    i_min = (A + Dmin)/2

    # Faixa de incidência em torno do mínimo
    i_vals = np.linspace(i_min - 0.2, i_min + 0.2, 300)
    D_vals = desvio(i_vals, n)

    # Plota curva
    plt.plot(i_vals, D_vals, color=cor, label=nome)

    # Marca o ponto do desvio mínimo
    plt.scatter([i_min], [Dmin], color=cor, edgecolor="k", zorder=5)
    print(cor, Dmin, n, delta_n)

plt.xlabel("Ângulo de incidência i (rad)")
plt.ylabel("Desvio angular D (rad)")
plt.title("Curvas D(i) para 7 comprimentos de onda")
plt.legend()
plt.grid(True)
plt.show()
