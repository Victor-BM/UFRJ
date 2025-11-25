import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import abc


class ProblemaExato:
    '''Representa a solução analítica da EDO
    '''
    def __init__ (self, f, f_derivada):
        self.f = f
        self.f_derivada = f_derivada

    def resolver_exato (self, x):
        return self.f(x)
    
    def derivada (self, x, y):
        return self.f_derivada(x, y)
    
class Solucionador (abc.ABC):
    def __init__ (self, nome, f, f_derivada):
        self.exata = ProblemaExato(f, f_derivada)
        self.nome = nome

    @abc.abstractmethod
    def resolver (self, h, x_final):
       pass

    def grafico (self, h, x_final):
        x_num, y_num = self.resolver(h, x_final)

        x_exata = np.linspace(0, x_final, 200)
        y_exata = self.exata.resolver_exato(x_exata)

        plt.figure(figsize = (8,5))
        plt.plot(x_exata, y_exata, 'k-', linewidth = 2, label = 'Solução Exata')
        plt.plot(x_num, y_num, 'r--o', label = f'{self.nome} (h = {h})')
        plt.title('Comparação de métodos')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.legend()
        plt.grid(True, linestyle = ':', alpha = 0.6)
        plt.show()

    def relatorio (self, lista_h, x_obj):
        resultados = []
        y_exata = self.exata.resolver_exato(x_obj)

        for h in lista_h:
            _, y_num = self.resolver(h, x_obj) #_ será ignorado
            y_obj = y_num[-1]
            erro_abs = abs(y_obj - y_exata)
            erro_rel = abs((erro_abs/y_exata)*100)

            resultados.append({
                'Passo (h)' : h, 
                'Valor Y(x) - Numérico' : y_obj,
                'Valor Y(x) - Exato' : y_exata,
                'Erro Absoluto' : erro_abs,
                'Erro Relativo (%)' : erro_rel,
                })
        df = pd.DataFrame(resultados)
        print(df.to_string(index=False, float_format=lambda x: "{:.6f}".format(x)))

class Euler (Solucionador):
    def __init__ (self, nome, f, f_derivada):
        Solucionador.__init__ (self, 'Euler', f, f_derivada)
    
    def resolver (self, h, x_final):
        x_values = np.arange(0, x_final + h/1000, h)
        y_values = np.zeros(len(x_values))
        y_values [0] = self.exata.f(0)

        f = self.exata.derivada

        for i in range (len(x_values) - 1):
            x, y = x_values[i], y_values[i]

            y_values[i+1] = y + (h*f(x, y))
        return x_values, y_values

class EulerModificado (Solucionador):
    def __init__ (self, nome, f, f_derivada):
        Solucionador.__init__ (self, 'Euler Modificado', f, f_derivada)
    
    def resolver (self, h, x_final):
        x_values = np.arange(0, x_final + h/1000, h)
        y_values = np.zeros(len(x_values))
        y_values [0] = self.exata.f(0)

        f = self.exata.derivada

        for i in range (len(x_values) - 1):
            x, y = x_values[i], y_values[i]

            k1 = f(x, y)
            y_pred = y + (h*k1)
            k2 = f(x+h, y_pred)

            y_values[i+1] = y + (h/2)*(k1 + k2)

        return x_values, y_values

class RungeKutta (Solucionador):
    def __init__ (self, nome, f, f_derivada):
        Solucionador.__init__ (self, 'Runge-Kutta 4ª', f, f_derivada)
    
    def resolver (self, h, x_final):
        x_values = np.arange(0, x_final + h/1000, h)
        y_values = np.zeros(len(x_values))
        y_values [0] = self.exata.f(0)

        f = self.exata.derivada

        for i in range (len(x_values) - 1):
            x, y = x_values[i], y_values[i]

            k1 = f(x, y)
            k2 = f(x+(h/2), y + h*(k1/2))
            k3 = f(x + (h/2), y + h*(k2/2))
            k4 = f(x + h, y + (h*k3))

            y_values[i+1] = y + (h/6)*(k1 + 2*k2 + 2*k3 + k4)

        return x_values, y_values

def f_2 (x):
    C = np.sqrt(3)
    return (0.0009*(x**2) - 0.06*C*x + (C**2))

def f_2_derivada (x, y):
    return -0.06*np.sqrt(y)

def main():
    h = 0.5
    x_obj = 5
    exato = ProblemaExato(f_2, f_2_derivada)
    euler = Euler('a', f_2, f_2_derivada)
    euler_modificado = EulerModificado('a', f_2, f_2_derivada)
    rk4 = RungeKutta('a', f_2, f_2_derivada)
    lista_h = [1, 2/3, 0.5, 0.25, 0.125]

    print(f'Solução Exata: {exato.resolver_exato(x_obj)}')
    print(f'Método de Euler: {euler.resolver(h, x_obj)[1][-1]}')
    print(f'Método de Euler Modificado: {euler_modificado.resolver(h, x_obj)[1][-1]}')
    print(f'Método de Runge-Kutta de 4ª Ordem: {rk4.resolver(h, x_obj)[1][-1]}\n\n\n')

    euler.grafico(h, x_obj)
    euler_modificado.grafico(h, x_obj)
    rk4.grafico(h, x_obj)

    euler.relatorio(lista_h, x_obj)
    print('\n\n\n')
    euler_modificado.relatorio(lista_h, x_obj)
    print('\n\n\n')
    rk4.relatorio(lista_h, x_obj)
    print('\n\n\n')

    print(f'Iterações - Método de Euler: {euler.resolver(h, x_obj)[1]}')
    print(f'Iterações - Método de Euler Modificado: {euler_modificado.resolver(h, x_obj)[1]}')
    print(f'Iterações - Método de Runge-Kutta de 4ª Ordem: {rk4.resolver(h, x_obj)[1]}\n\n\n')
main()