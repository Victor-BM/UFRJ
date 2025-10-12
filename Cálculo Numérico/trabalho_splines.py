'''
Trabalho Splines - Cálculo Numérico

Prof: Maria Helena

Aluno: Gabriel Peixoto Costa Marques Barbosa          DRE: 124026590
Aluno: Felipe Mariano Lessa Chaves                    DRE: 124055298
Aluno: Víctor Bernardes de Morais                     DRE: 124031375

Feito no VSCode com Python 3.11.3
'''

import numpy as np
import scipy as sc
import matplotlib.pyplot as plt
import abc

class Spline (abc.ABC):
    def __init__ (self, x, y):
        self.x = np.array(x, dtype=float)
        self.y = np.array(y, dtype=float)
        self.grau = len(self.x) - 1

    def encontrar_intervalo(self, t):
        for i in range(self.grau):
            if self.x[i] <= t <= self.x[i+1]:
                return i
        return None

    def plotar (self):
        fig, ax = plt.subplots()
        ax.plot(self.x, self.y, 'o', label='Dados originais')
        ax.set_xlabel('t (s)')
        ax.set_ylabel('v (m/s)')
        ax.grid(True)
        return ax
    
    @abc.abstractmethod
    def interpolar (self, t):
        pass

    @abc.abstractmethod
    def calcular_coeficientes (self):
        pass
        
class SplineLinear (Spline):
    def __init__ (self, x, y):
        Spline.__init__(self, x, y)
        self.coeficientes = self.calcular_coeficientes()
    
    def calcular_coeficientes (self):
        coefs = []
        for i in range (self.grau):
            t_i, v_i = self.x[i], self.y[i]
            t_i1, v_i1 = self.x[i+1], self.y[i+1]
            m_i = (v_i1 - v_i)/(t_i1 - t_i)

            coefs.append({'i': i, 't_i': t_i, 'v_i' : v_i, 'm_i' : m_i})
        return coefs
    
    def interpolar(self, t):
        i = self.encontrar_intervalo(t)
        segmento = self.coeficientes[i]
        velocidade = segmento['v_i'] + segmento['m_i']*(t - segmento['t_i'])
        return velocidade

    def plotar (self):
        fig, ax = plt.subplots(figsize=(10, 6))

        t_vals = np.linspace(self.x[0], self.x[-1], 300)
        v_vals = [self.interpolar(t) for t in t_vals]

        ax.scatter(self.x, self.y, label='Pontos Originais', 
           color='green', marker='o', s=50, zorder=4)
        
        ax.scatter(16, self.interpolar(16), 
           label=f'$t={16}$s (Interpolação)', 
           color='red', marker='X', s=50, zorder=4)

        ax.plot(t_vals, v_vals, label = 'Spline Linear', color = 'blue')
        ax.set_xlabel('t (s)')
        ax.set_ylabel('v (m/s)')
        ax.legend()
        ax.grid(linestyle = ':')
        plt.show()

class SplineQuadratico (Spline):
    def __init__ (self, x, y):
        Spline.__init__(self, x, y)
        self.coeficientes = self.calcular_coeficientes()
    
    def calcular_coeficientes(self):
        n = self.grau
        num_equações = 3*n
        A = np.zeros((num_equações, num_equações))
        B = np.zeros(num_equações)
        count = 0
        
        for i in range (n):
            '''relacionando os valores das funções quadráticas nos extremos'''
            A[count, 3*i] = (self.x[i])**2   #a
            A[count, 3*i + 1] = (self.x[i])  #b
            A[count, 3*i + 2] = 1            #c
            B[count] = (self.y[i])
            count += 1

            A[count, 3*i] = (self.x[i+1])**2   #a
            A[count, 3*i + 1] = (self.x[i+1])  #b
            A[count, 3*i + 2] = 1              #c
            B[count] = (self.y[i+1])
            count += 1

        for i in range (1, n):
            '''relacionando os valores das derivadas das funções quadráticas'''
            A[count, 3*(i-1)] = 2*self.x[i]    #a_i 
            A[count, 3*(i-1) + 1] = 1          #b_i 
            A[count, 3*i] = -2*self.x[i]   #a_i+1 
            A[count, 3*i + 1] = -1             #b_i+1 
            B[count] = 0
            count += 1
        
        A[count, 0] = 1
        B[count] = 0
        count += 1

        try:
            coefs = sc.linalg.solve (A, B) #método que usa decomposição LU para calcular os coeficientes
        except Exception:
            print('erro')
            return np.array([])
        return coefs.reshape (n, 3)
    
    def interpolar(self, t):
        try:
            i = self.encontrar_intervalo(t)
            a, b, c = self.coeficientes[i]
            velocidade = a*(t**2) + b*t +c
        except ValueError:
            return np.nan
        return velocidade
    
    def derivar (self, t):
        i = self.encontrar_intervalo(t)
        a, b, c = self.coeficientes[i]
        aceleracao = 2*a*(t) + b
        return aceleracao
    
    def integrar (self, t_inicio, t_fim):
        distancia = 0
        def primitiva (t, a, b, c):
            return  (a/3)*(t**3) + (b/2)*(t**2) + (c*t)
        
        i_inicio = self.encontrar_intervalo(t_inicio)
        i_fim = self.encontrar_intervalo(t_fim)
        
        for i in range (i_inicio, i_fim + 1):
            '''secciona o intervalo de integração entre as funções que abrangem esse intervalo'''
            a, b, c = self.coeficientes[i]

            inferior = max(t_inicio, self.x[i])
            superior = min(t_fim, self.x[i+1])

            distancia_parcial = primitiva(superior, a, b, c) - primitiva(inferior, a, b, c)
            distancia += distancia_parcial
        return distancia

    def plotar (self):
        fig, ax = plt.subplots(figsize=(10, 6))

        t_vals = np.linspace(self.x[0], self.x[-1], 300)
        v_vals = [self.interpolar(t) for t in t_vals]

        ax.scatter(self.x, self.y, label='Pontos Originais', 
           color='green', marker='o', s=50, zorder=4)
        
        ax.scatter(16, self.interpolar(16), 
           label=f'$t={16}$s (Interpolação)', 
           color='red', marker='X', s=50, zorder=4)

        ax.plot(t_vals, v_vals, label = 'Spline Quadrático', color = 'blue')
        ax.set_xlabel('t (s)')
        ax.set_ylabel('v (m/s)')
        ax.legend()
        ax.grid(linestyle = ':')
        plt.show()

def main():
    tempos = [0, 10, 15, 20, 22.5, 30]
    velocidades = [0, 227.04, 362.78, 517.35, 602.97, 901.67]
    #1.1
    spline_linear = SplineLinear(tempos, velocidades)
    print (f'Usando splines lineares: v(16) = {spline_linear.interpolar(16):.2f} m/s')
    spline_linear.plotar()
    #1.2 - a
    spline_quadratico = SplineQuadratico(tempos, velocidades)
    print (f'Usando splines quadráticos: v(16) = {spline_quadratico.interpolar(16):.2f} m/s')
    spline_quadratico.plotar()
    #1.2 - b
    print (f'Usando splines quadráticos: a(16) = {spline_quadratico.derivar(16):.2f} m/s²')
    #1.2 - c
    print (f'Usando splines quadráticos: s(16) - s(11) = {spline_quadratico.integrar(11, 16):.2f} m')

main()