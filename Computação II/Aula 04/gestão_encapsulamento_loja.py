class Produto:
    def __init__ (self, preço, descrição):
        self.__preço = float(preço)
        self.__descrição = descrição
    
    def get_info (self):
        return(f'{self.__descrição}: {self.__preço}')

class ProdutoImportado (Produto):
    def __init__(self, preço, descrição, taxa_importação):
        super().__init__(preço, descrição)
        self.__taxa_importação = float(taxa_importação)
    
    def get_info(self):
        pai = Produto.get_info(self)
        info, valor = '', ''
        j = len(pai)
        for i in range(len(pai)):
            if pai[i] == ':':
                j = i
            if i < j:
                info += pai[i]
            elif i > (j + 1) :
                valor += pai[i]
        valor = float(valor)
        return (f'{info}: {valor*(1+self.__taxa_importação)}')

banana = Produto(5, 'banana')
banana.__preço = 6
print(banana.get_info())
maçã = ProdutoImportado(100, 'maça', 0.5)
print(maçã.get_info())

#nesse caso, faz mais sentidos usar o método get_info, mas no outro código v2 tem usando property