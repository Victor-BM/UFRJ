import numpy as np
import abc

class Integracao (abc.ABC):
    def __init__ (self, a, b, n, f):
        self.a = a
        self.b = b
        self.n = n
        self.f = f
        self.h = (b - a)/n

    @abc.abstractmethod 
    def resolver (self):
       pass

class TrapezioRepetido (Integracao):
    def __init__ (self, a, b, n, f):
        Integracao.__init__(self, a, b, n, f)
    
    def resolver(self):
        somatorio = 0
        for i in range(1, self.n):
            x_i = self.a + i*self.h
            somatorio += self.f(x_i)
        soma = self.f(self.a) + 2*somatorio + self.f(self.b)
        print(f'Trapézio Repetido (n = {self.n}) = {(self.h/2)*soma}')

class SimpsonRepetido_terco (Integracao):
    def __init__ (self, a, b, n, f):
        Integracao.__init__(self, a, b, n, f) #n par
    
    def resolver(self):
        somatorio_impar = 0
        somatorio_par = 0
        for i in range(1, self.n, 2):
            x_i = self.a + i*self.h
            somatorio_impar += self.f(x_i)
        for j in range(2, self.n, 2):
            x_j = self.a + j*self.h
            somatorio_par += self.f(x_j)
        soma = self.f(self.a) + 4*somatorio_impar + 2*somatorio_par + self.f(self.b)
        print(f'Simpson Repetido 1/3 (n = {self.n}) = {(self.h/3)*soma}')

class SimpsonRepetido_3oitavos (Integracao):
    def __init__ (self, a, b, n, f):
        Integracao.__init__(self, a, b, n, f) #n múltiplo de 3
    
    def resolver(self):
        somatorio = 0
        for i in range(1, self.n):
            x_i = self.a + i*self.h
            if i%3 == 0:
                somatorio += 2*self.f(x_i)
            else:
                somatorio += 3*self.f(x_i)
        soma = self.f(self.a) + somatorio + self.f(self.b)
        print(f'Simpson Repetido 3/8 (n = {self.n}) = {3*(self.h/8)*soma}')

class QuadraturaGaussiana (Integracao):
    def __init__ (self, a, b, n, f):
        Integracao.__init__(self, a, b, n, f) #n não é usado, pq n=2
    
    def resolver(self):
        media = (self.a + self.b)/2
        diferenca_raiz = (self.b - self.a)/(2*np.sqrt(3))
        soma = self.f(media - diferenca_raiz) + self.f(media + diferenca_raiz)
        print(f'Quadratura Gaussiana = {((self.b - self.a)/2)*soma}')

def f (x):
    'insira a fórmula do seu f(x) no return'
    return None

def f_a (x):
    return np.exp(x)
def f_b (x):
    return np.sqrt(x)
def f_c (x):
    return 1/x

def Q1():
    print('Questão 1 - a')
    resultado = TrapezioRepetido(1, 2, 4, f_a)
    resultado.resolver()
    resultado= TrapezioRepetido(1,2, 6, f_a)
    resultado.resolver()
    print('\n')
    resultado = SimpsonRepetido_terco(1, 2, 4, f_a)
    resultado.resolver()
    resultado= SimpsonRepetido_terco(1,2, 6, f_a)
    resultado.resolver()
    print('\n\n\nQuestão 1 - b')
    resultado = TrapezioRepetido(1, 4, 4, f_b)
    resultado.resolver()
    resultado= TrapezioRepetido(1,4, 6, f_b)
    resultado.resolver()
    print('\n')
    resultado = SimpsonRepetido_terco(1, 4, 4, f_b)
    resultado.resolver()
    resultado= SimpsonRepetido_terco(1, 4, 6, f_b)
    resultado.resolver()
    print('\n\n\nQuestão 1 - c')
    resultado = TrapezioRepetido(2, 14, 4, f_c)
    resultado.resolver()
    resultado= TrapezioRepetido(2, 14, 6, f_c)
    resultado.resolver()
    print('\n')
    resultado = SimpsonRepetido_terco(2, 14, 4, f_c)
    resultado.resolver()
    resultado= SimpsonRepetido_terco(2 ,14, 6, f_c)
    resultado.resolver()

def f_3 (x):
    return 1/(1+x)

def Q3():
    resultado = TrapezioRepetido(0, 0.6, 9, f_3)
    resultado.resolver()
    resultado = SimpsonRepetido_terco(0, 0.6, 4, f_3)
    resultado.resolver()
    resultado = SimpsonRepetido_3oitavos(0, 0.6, 6, f_3)
    resultado.resolver()

def f_5 (x):
    return 3*(x**3) - 3*x + 1

def Q5():
    resultado = TrapezioRepetido(0, 4, 4, f_5)
    resultado.resolver()
    resultado = SimpsonRepetido_terco(0, 4, 4, f_5)
    resultado.resolver()

def f_9 (x):
    return np.exp(x) + x**2

def Q9():
    resultado = TrapezioRepetido(0, 1, 3, f_9)
    resultado.resolver()

def Q10 ():
    resultado = QuadraturaGaussiana(3, 3.6, 2, f_c)
    resultado.resolver()
    resultado = SimpsonRepetido_terco(3, 3.6, 4, f_c)
    resultado.resolver()
    resultado = TrapezioRepetido(3, 3.6, 116, f_c)
    resultado.resolver()

def f_13 (x):
    return np.exp(-(x**2))

def Q13 ():
    resultado = QuadraturaGaussiana(0,1, 2, f_13)
    resultado.resolver()
    resultado = SimpsonRepetido_terco(0, 1, 4, f_13)
    resultado.resolver()
    resultado = TrapezioRepetido(0, 1, 17, f_13)
    resultado.resolver()
Q13()