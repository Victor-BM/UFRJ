class ValorInvalidoException (Exception):
    def __init__(self):
        pass

class SaldoInsuficienteException (Exception):
    def __init__ (self):
        pass

class ContaBancaria:
    def __init__ (self, saldo_incial: float):
        self.__saldo = saldo_incial
    
    @property
    def saldo (self):
        return self.__saldo
    
    @saldo.setter
    def saldo (self, valor : float):
        try:
            if valor < 0:
                raise ValorInvalidoException
        except ValorInvalidoException:
            print('O saldo não pode ser negativo')
        else:
            self.__saldo = valor

    def depositar (self, valor : float):
        try:
            if valor < 0:
                raise ValorInvalidoException
        except Exception as erro:
            print('Não é possível depositar um valor negativo')
        else:
            self.saldo += valor
            print(f'Novo saldo: {self.saldo}')

    def sacar (self, valor : float):
        try:
            if valor < 0:
                raise ValorInvalidoException
            if valor > self.saldo:
                raise SaldoInsuficienteException
        except ValorInvalidoException:
            print('Erro ao sacar: Não é possível sacar um valor negativo')
        except SaldoInsuficienteException as erro:
            print(f'{erro.__class__.__name__}: Saldo insuficiente para sacar {valor}. Saldo atual: {self.saldo}')
        else:
            self.saldo -= valor
            print(f'Novo saldo: {self.saldo}')

def main():
    print('Bem-vindo ao Banco do LP!\n')
    conta1 = ContaBancaria(0)
    while True:
        try:
            saldo_inicial = float(input('Digite o saldo inicial da sua conta: '))
            conta1.saldo = saldo_inicial
            if conta1.saldo == saldo_inicial:
                print(f'Saldo atual: {conta1.saldo}')
                break
        except Exception as erro:
            print(f'Erro: {erro.__class__.__name__}')
    while True:
        print('\nOpções disponíveis:\n1 - Depositar\n2 - Sacar\n3 - Consultar saldo\n0 - Sair\n')
        try:
            option = int(input('Escolha uma opção: '))
        except:
            print('Opção inválida! Escolha um número de 0 a 3')
        else:
            try:
                if option == 0:
                    print('Saindo...\nObrigado por usar nossos serviços!')
                    break
                elif option == 1:
                    depósito = float(input('Digite o novo valor que deseja depositar: '))
                    conta1.depositar(depósito)
                elif option == 2:
                    saque = float(input('Digite o valor que deseja sacar: '))
                    conta1.sacar(saque)
                elif option == 3:
                    print(f'Saldo atual: {conta1.saldo}')
                else:
                    print('Opção inválida')
            except Exception as erro:
                print(f'Erro: {erro.__class__.__name__}')

if __name__ == '__main__':
    main()
