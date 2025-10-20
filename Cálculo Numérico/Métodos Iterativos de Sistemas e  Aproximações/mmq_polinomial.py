import numpy as np
import matplotlib.pyplot as plt
import scipy as sc

class MMQ_Polinomial:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.coefs = np.array([])
        self.resíduo = 0.0

    def dispersão (self):
        plt.scatter(self.x, self.y)
        plt.title('Gráfico de Dispersão')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.grid()
        plt.show()
    
    def calcular_coefs (self, grau):
        A = np.zeros((len(self.x), grau + 1))
        B = np.zeros(len(self.x))
        for i in range (len(self.x)):
            for j in range (grau + 1):
                A[i, j] = self.x[i]**j
            B[i] = self.y[i]
        A_transposta = A.T
        C = np.matmul(A_transposta, A)
        D = np.matmul(A_transposta, B)
        try:
            self.coefs = sc.linalg.solve (C, D) #método que usa decomposição LU para calcular os coeficientes
        except Exception:
            print('erro')
            return np.array([])
    
    def calcular_polinomio (self, t):
        resultado = 0.0
        for i in range (len(self.coefs)):
            resultado += self.coefs[i]*(t**i)
        return resultado
    
    def erro_residual (self):
        soma = 0.0
        for i in range (len(self.x)):
            soma += (self.y[i] - self.calcular_polinomio(self.x[i]))**2
        self.resíduo = soma
        return self.resíduo

    def gráfico (self):

        t_vals = np.linspace(self.x[0], self.x[-1], 300)
        v_vals = [self.calcular_polinomio(t) for t in t_vals]

        plt.scatter(self.x, self.y, label='Pontos Originais', color='green', marker='o', s=50, zorder=4)

        plt.plot(t_vals, v_vals, label = 'MMQ', color = 'blue')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Método dos Mínimos Quadrados')
        plt.legend()
        plt.grid(linestyle = ':')
        plt.show()

def main():
    X = np.array([1.000, 0.970, 0.883, 0.750, 0.587, 0.413, 0.250, 0.117, 0.030, 0.000, 0.030]) 
    Y = np.array([0.58, 0.58, 0.56, 0.53, 0.50, 0.46, 0.43, 0.40, 0.39, 0.37, 0.38])
    polinomial = MMQ_Polinomial(X, Y)
    polinomial.dispersão()
    polinomial.calcular_coefs(1)
    polinomial.erro_residual()
    print(polinomial.coefs)
    print(polinomial.resíduo)
    polinomial.gráfico()    
main()
