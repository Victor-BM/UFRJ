import pickle
import abc
import os

class ContaBancaria (abc.ABC):
    def __init__ (self, numero : int, saldo : float):
        self.numero = numero
        self._saldo = saldo
    
    @property
    def saldo (self):
        return self._saldo
    
    @saldo.setter
    def saldo (self, valor):
        self._saldo = valor
    
    @abc.abstractmethod
    def operacao (self, entrada : float):
        pass

    def __str__ (self):
        return f'Número: {self.numero} - Saldo: R$ {self.saldo:.2f}'

class ContaCorrente (ContaBancaria):
    def __init__ (self, numero : int, saldo : float, limite : float):
        ContaBancaria.__init__ (self, numero, saldo)
        self.limite = 100
        if 100 <= limite <= 1000:
            self.limite = limite
    
    def operacao(self, entrada : float):
        if entrada >= 0: #depósito
            self.saldo += entrada
        else: #saque
            if (entrada + self.saldo) >= 0:
                self.saldo += entrada
            elif (entrada + self.saldo) >= (-self.limite):
                print('Aplicando limite')
                self.saldo += entrada
            else:
                print('Saldo insuficiente')
    
    def __str__ (self):
        return f'{ContaBancaria.__str__(self)}' + f' - Limite Especial: R$ {self.limite:.2f}'

class ContaPoupança (ContaBancaria):
    def __init__ (self, numero : int, saldo : float, taxa : float):
        ContaBancaria.__init__(self, numero, saldo)
        taxa = taxa
        self.taxa = 0.1
        if 0.1 <= taxa <= 0.5:
            self.taxa = taxa
    
    def operacao(self, entrada : float):
        if entrada >= 0: #depósito
            self.saldo += entrada
        else: #saque
            if (entrada + self.saldo) >= 0:
                self.saldo += entrada
            else:
                print('Saldo insuficiente')
    
    def aplicar_rendimento (self):
        self.saldo += (self.saldo*(self.taxa/100))
    
    def __str__(self):
        return f'{ContaBancaria.__str__(self)}' + f' - Taxa de Rendimento: {self.taxa:.2f}%'

class Banco:
    def __init__(self):
        self.contas = {}
    
    def cadastrar (self, numero, conta):
        if numero not in self.contas:
            self.contas[numero] = conta
            print(f'Conta {numero} cadastrada!')
        else:
            print(f'Conta {numero} já cadastrada!')
    
    def excluir (self, numero):
        try:
            del self.contas[numero]
            print(f'Conta {numero} excluída!')
        except:
            print(f'Conta {numero} não cadastrada')
    
    def alterar_dados (self, numero, saldo = None, particularidade = None):
        if numero in self.contas:
            conta = self.contas[numero]
            if saldo:
                conta.saldo = saldo
            if particularidade:
                if isinstance(conta, ContaCorrente):
                    conta.limite = particularidade
                if isinstance(conta, ContaPoupança):
                    conta.taxa = particularidade
            print(f'Informaçãoes da conta {numero} alteradas')
        else:
            print(f'Conta {numero} não cadastrada')
    
    def listar (self):
        if len(self.contas) == 0:
            print('Nenhuma conta cadastrada no banco')
        else:
            for conta in self.contas.values():
                print(f'{conta.__class__.__name__}: ' + f'{conta.__str__()}')
    
    def salvar_dados (self):
        if len(self.contas) > 0:
            with open('contas.pkl', 'wb') as file:
                pickle.dump(self.contas, file)
            print('Objetos salvos com sucesso em conta.pkl')
        else:
            print('Não foi possível salvar')
    
    def carregar_dados (self):
        try:
            with open ('contas.pkl', 'rb') as file:
                self.contas = pickle.load(file)
        except Exception as erro:
            print(f'{erro.__class__}')

Banco = Banco()
Banco.carregar_dados()

def menu():
    print('\nMenu Principal')
    print(('1. Cadastrar Conta\n2. Listar Contas\n3. Excluir Conta\n4. Alterar Conta\n5. Sair'))

def testar_especial(valor):
    '''Para permitir que o usuário mantenha uma informação ao alterar dados'''
    try:
        valor = float(valor)
        return valor
    except:
        return None

def main():
    while True:
        menu()
        try:
            escolha = int(input('Escolha uma opção: '))
            os.system('cls')
        except:
            print('Opção inválida! Digite um número inteiro de 1 a 5')
        else:
            if escolha == 1:
                try:
                    numero = int(input('Digite o número da conta: '))
                    saldo = float(input('Digite o saldo inicial da conta: '))
                    tipo_conta = input('A conta é do tipo ContaCorrente ou ContaPoupança? ').lower()
                    if tipo_conta == 'contacorrente':
                        limite = float(input('Digite um limite especial de R$100.00 a R$1000.00: '))
                        conta00 = ContaCorrente(numero, saldo, limite)
                        Banco.cadastrar(numero, conta00)
                    elif tipo_conta == 'contapoupança' or tipo_conta == 'contapoupanca':
                        taxa = float(input('Digite uma taxa de rendimento de 0.1 a 0.5: '))
                        conta00 = ContaPoupança(numero, saldo, taxa)
                        Banco.cadastrar(numero, conta00)
                    else:
                        print('Opção de tipo de conta inválida')
                except Exception as erro:
                    print(f'Erro! {erro.__class__}')
            elif escolha == 2:
                Banco.listar()
            elif escolha == 3:
                try:
                    numero = int(input('Digite o número da conta a ser excluída do cadastro: '))
                    Banco.excluir(numero)
                except Exception as erro:
                    print(f'Erro! {erro.__class__}')
            elif escolha == 4:
                try:
                    numero = int(input('Digite o número da conta a ser alterada: '))
                except Exception as erro:
                    print(f'Erro! {erro.__class__}')
                else:
                    saldo = input('Digite o novo saldo conta (aperte Enter para manter): ')
                    saldo = testar_especial(saldo)
                    tipo_conta = input('A conta é do tipo ContaCorrente ou ContaPoupança? ').lower()
                    if tipo_conta == 'contacorrente':
                        particularidade = input('Digite o novo limite especial de R$100.00 a R$1000.00 (aperte Enter para manter): ')
                        particularidade = testar_especial(particularidade)
                        Banco.alterar_dados(numero, saldo, particularidade)
                    elif tipo_conta == 'contapoupança' or tipo_conta == 'contapoupanca':
                        particularidade = input('Digite o novo taxa de rendimento de 0.1 a 0.5 (aperte Enter para manter): ')
                        particularidade = testar_especial(particularidade)
                        Banco.alterar_dados(numero, saldo, particularidade)
                    else:
                        print('Opção de tipo de conta inválida')
            elif escolha == 5:
                Banco.salvar_dados()
                break
            else:
                print('Opção inválida! Digite um número inteiro de 1 a 5')

if __name__ == '__main__':
    main()