import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Dados: (cor, lambda (Å), Dmin em graus)
data = [
    ("Amarelo 1", 5791, 50 + 12.5/60),
    ("Amarelo 2", 5770, 50 + 12.5/60),
    ("Verde", None, 50 + 11.5/60),                       # sem λ
    ("Verde-Azul", 4916, 50 + 12.5/60),
    ("Azul-Anil", 4358, 49 + 14/60),
    ("Violeta 1", 4078, 49 + 35/60),
    ("Violeta 2", 4047, 49 + 52/60),
]

A = np.deg2rad(60)  # Ângulo do prisma em radianos

# Listas para armazenar resultados
lambdas = []
inv_lambda2 = []
n_vals = []

lambdas_tabela = []
inv_lambda_tabela = []
n_tabela = ['16403.9e-04', '16403.9e-04', '16402.2e-04', '16403.9e-04', '16305.9e-04', '16341.2e-04', '16369.7e-04']
cores = ['Amarelo 1', 'Amarelo 2', 'Verde', 'Verde-Azul', 'Azul-Anil', 'Violeta 1', 'Violeta 2']

for cor, lam, Dmin_deg in data:
    Dmin = np.deg2rad(Dmin_deg)
    n = np.sin((A + Dmin) / 2) / np.sin(A / 2)
    if lam == None:
        lambdas_tabela.append(np.nan)
        inv_lambda_tabela.append(np.nan)
    else:
        lambdas.append(lam)
        lambdas_tabela.append(lam)
        inv_lambda_tabela.append((1. / lam**2))
        inv_lambda2.append(1. / lam**2)  # λ^-2
        n_vals.append(n)

# Converter para arrays
lambdas = np.array(lambdas)
inv_lambda2 = np.array(inv_lambda2)
n_vals = np.array(n_vals)

# Ajuste linear: n = b * λ^-2 + a
coef = np.polyfit(inv_lambda2, n_vals, 1)  # coef[0] = b, coef[1] = a
b, a = coef[0], coef[1]

# Reta ajustada
fit_line = b*inv_lambda2 + a

# --- Tabela ---
df = pd.DataFrame({
    'Cor': cores,
    "λ (Å)": lambdas_tabela,
    "λ^-2 (1/Å²)": inv_lambda_tabela,
    "n(λ)": n_tabela,
    "δ_n(λ)": '0.8e-04'
})
print(df)
df.to_csv('tabela_exp2.csv', index=False)
print(f"\nParâmetros ajustados: a = {a:.6f}, b = {b:.6e}")

# --- Gráfico ---
# Define o erro de n. Como n é o eixo Y, usamos yerr.
erro_n = 0.8e-5

plt.figure(figsize=(7,5))

# Use plt.errorbar para plotar os pontos com as barras de erro
# O argumento 'yerr' define o erro no eixo vertical (eixo y), que é o seu n(λ)
plt.errorbar(inv_lambda2, n_vals, yerr=erro_n, fmt='o', color="red", label="Dados experimentais com erro")

# Plota a reta ajustada
plt.plot(inv_lambda2, fit_line, color="blue", label=f"Ajuste linear: n = {b:.2e} λ⁻² + {a:.3f}")

# Rótulos dos eixos
plt.xlabel("λ⁻² (1/Å²)")
plt.ylabel("n(λ)")

plt.title("Ajuste linear de n(λ) em função de λ⁻²")
plt.legend()
plt.grid(True)
plt.show()
