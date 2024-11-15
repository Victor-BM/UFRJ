class ListaNumeros:
    def __init__ (self):
        self.numeros = []
    
    def somar (self, num1, num2):
        try:
            print(f'{num1 + num2}')
        except:
            print('Erro: Todos os argumentos devem ser números.')
    
    def subtrair (self, num1, num2):
        try:
            print(f'{num1 - num2}')
        except:
            print('Erro: Todos os argumentos devem ser números.')
    
    def adicionar_numero (self, num):
        try:
            num = int(num)
        except ValueError:
            print('Erro: O número a ser adicionado deve ser um inteiro.')
        else:
            self.numeros.append(num)
    
    def remover_numero (self):
        try:
            self.numeros.pop()
        except IndexError:
            print('Erro: A lista está vazia, não há números para remover.')

lista = ListaNumeros()
lista.somar(10, 'abc')
lista.subtrair('abc', 5)
lista.adicionar_numero('abc')
lista.remover_numero()
lista.remover_numero()