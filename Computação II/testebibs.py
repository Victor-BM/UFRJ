import matplotlib.pyplot as plt
import numpy as np
import tkinter as tk
import PyQt6 as pyq
import turtle as trt
import pandas as pnd


#CHATGPT

# Passo 1: Criar dados
theta = np.linspace(0, 2 * np.pi, 100)  # 100 pontos de 0 a 2π
x = np.cos(theta)  # Coordenada x do círculo
y = np.sin(theta)  # Coordenada y do círculo

# Passo 2: Criar o gráfico
plt.figure(figsize=(6, 6))  # Tamanho da figura
plt.plot(x, y, label='Círculo', color='blue')  # Desenhar o círculo
plt.fill(x, y, color='lightblue', alpha=0.5)  # Preencher o círculo

# Passo 3: Personalizar o gráfico
plt.title('Desenho de um Círculo')  # Título do gráfico
plt.xlabel('Eixo X')  # Rótulo do eixo X
plt.ylabel('Eixo Y')  # Rótulo do eixo Y
plt.axhline(0, color='black',linewidth=0.5, ls='--')  # Linha horizontal
plt.axvline(0, color='black',linewidth=0.5, ls='--')  # Linha vertical
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)  # Grade
plt.axis('equal')  # Igualar as proporções dos eixos
plt.legend()  # Mostrar legenda

# Passo 4: Exibir o gráfico
plt.show()
