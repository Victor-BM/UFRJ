class Conta:
    def __init__ (self, numero_conta:int, saldo:float):
        if isinstance(numero_conta, int) and isinstance(saldo, float) and saldo > 0:
            self.numero_conta = numero_conta
            self.saldo = saldo
        else:
            print ('Erro, instanciação cancelada')
            return 
        
    def depositar (self, valor):
        self.saldo += valor
    
    def sacar (self, valor):
        if (self.saldo - valor) > 0:
            self.saldo -= valor
        else:
            return 'Saldo insuficiente'

class ContaCorrente (Conta):
    def __init__(self, numero_conta, saldo, limite_cheque_especial):
        Conta.__init__(self, numero_conta, saldo)
        if isinstance(limite_cheque_especial, float):
            self.limite_cheque_especial = limite_cheque_especial
        else:
            print ('Erro, instanciação cancelada')
            return 
    
    def usar_cheque_especial (self, valor):
        if self.sacar(valor) == 'Saldo insuficiente':
            self.saldo = max(self.saldo - valor, self.saldo - self.limite_cheque_especial)

class ContaPoupança (Conta):
    def __init__(self, numero_conta, saldo, taxa_juros):
        Conta.__init__(self, numero_conta, saldo)
        if isinstance(taxa_juros, float):
            self.taxa_juros = taxa_juros
        else:
            print ('Erro, instanciação cancelada')
            return 
        
    def calcular_juros (self):
        juros = self.saldo*self.taxa_juros
        self.depositar(juros)

poup1 = ContaPoupança (3234, 100.5, 0.05)
poup1.calcular_juros()
print(poup1.saldo)
corr = ContaCorrente(4343, 50.0, 100.0)
corr.usar_cheque_especial(200)
print(corr.saldo)