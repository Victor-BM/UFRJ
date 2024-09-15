class Produto:
    def __init__ (self, nome, preço):
        self.nome = nome
        self.preço = preço
    
    def exibir_detalhes(self):
        return f'Nome: {self.nome}\nPreço: ${self.preço}'

class Eletrônico (Produto):
    def __init__(self, nome, preço, garantia, marca):
        Produto.__init__(self, nome, preço)
        self.garantia = garantia
        self.marca = marca
    
    def mostrar_garantia (self):
        return f'Garantia: {self.garantia} anos'

class Smathphone (Eletrônico):
    def __init__(self, nome, preço, garantia, marca, sistema_operacional, capacidade_armazenamento):
        Eletrônico.__init__(self, nome, preço, garantia, marca)
        self.sistema_operacional = sistema_operacional
        self.capacidade_armazenamento = capacidade_armazenamento
    
    def exibir_especificações (self):
        return f'{self.exibir_detalhes()}\n{self.mostrar_garantia()}\nSistema Operacional: {self.sistema_operacional}\nArmazenamento: {self.capacidade_armazenamento}GB'
    
produto = Produto("Cadeira", 50)
print(produto.exibir_detalhes())
print('\n\n')
notebook = Eletrônico("Notebook", 800, 2, "Dell")
print(notebook.exibir_detalhes())
print(notebook.mostrar_garantia())
print('\n\n')
celular = Smathphone("Pixel", 600, 2, "Google", "Android", 128)
print(celular.exibir_especificações())