class ValorInvalidoException (Exception):
     def __init__(self, mensagem = 'Erro de valor inválido'):
          self.mensagem = mensagem
          super().__init__(self.mensagem)

class SaldoInsuficienteException (Exception):
     def __init__(self, mensagem = 'Valor inválido'):
          self.mensagem = mensagem
          super().__init__(self.mensagem)

def verificar_negativo(valor):
     if valor > 0:
          return True
     else:
          raise ValorInvalidoException

def verificar_saldo(saldo, saque):
     if saque <= saldo:
          return True
     else:
          raise SaldoInsuficienteException

class ContaBancaria:
    def __init__ (self, saldo_inicial:float):
            self.__saldo = saldo_inicial
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo (self, valor:float):
        try:
            if verificar_negativo(valor):
                self.__saldo = valor
        except ValorInvalidoException as error:
            print(f'O saldo não pode ser negativo')
    
    def depositar (self, depósito:float):
        try:
            if verificar_negativo(depósito):
                self.saldo += depósito
                print(f'Novo saldo: {self.saldo}')
        except ValorInvalidoException as error:
            print('Não é possível depositar um valor negativo')
    
    def sacar (self, saque: float):
        try:
            if verificar_negativo(saque):
                try:
                    if verificar_saldo(self.saldo, saque):
                        self.saldo -= saque
                        print(f'Novo saldo: {self.saldo}')
                except SaldoInsuficienteException as error:
                     print(f'SaldoInsuficienteException: {error.mensagem}. Saldo insuficiente para sacar {saque}. Saldo atual {self.saldo}')
        except ValorInvalidoException as error:
            print('Erro ao sacar. Não é possível sacar um valor negativo')

def main ():
    conta1 = ContaBancaria(0)
    print('Bem-vindo ao Banco do LP!')
    while True:
        try:
            saldo = float(input('Digite o saldo inicial da sua conta: '))
            conta1.saldo = saldo
            if conta1.saldo == saldo:
                print(f'Saldo atual: {conta1 .saldo}')
                break
        except:
            print('Opção inválida')
    while True:
        print('\nOpções disponíveis:\n1 - Depositar\n2 - Sacar\n3 - Consultar Saldo\n0 - Sair\n')
        try:
            escolha = int(input('Escolha uma opção: '))
            if escolha == 0:
                print('Saindo...\nObrigado por usar nossos serviços')
                break
            elif escolha == 1:
                try:
                    depósito = float(input('Digite o valor que deseja depositar: '))
                    depósito = float(depósito)
                    conta1.depositar(depósito)
                except:
                    print('Opção inválida')
            elif escolha == 2:
                try:
                    saque = float(input('Digite um valor que deseja sacar: '))
                    saque = float(saque)
                    conta1.sacar(saque)
                except:
                    print('Opção inválida')
            elif escolha == 3:
                print(f'Saldo atual: {conta1.saldo}')
            else:
                print('Opção inválida')
        except:
            print('Opção inválida')
main()