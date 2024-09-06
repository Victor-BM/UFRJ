class Livro:#gera objeto
    def __init__ (self, titulo, autor, preco, estado):
        self.titulo = titulo
        self.autor = autor
        self.preco = float(preco)
        self.estado = self.validar_estado(estado)

    def validar_estado(self,estado):
        estados_validos=['novo', 'semi-novo', 'desgastado', 'deplorável']
        if estado.lower() in estados_validos:
            return estado.lower()
        else:
            print('Estado inválido!')
            return 'desconhecido'
        
    def calcular_preco(self):
        if self.estado == 'novo':
            return self.preco
        elif self.estado == 'semi-novo':
            return self.preco*0.9
        elif self.estado == 'desgastado':
            return self.preco*0.75
        elif self.estado == 'deplorável':
            return self.preco*0.5
        else:
            self.preco = 'desconhecido'
            return self.preco
    
    def exibir_informacao(self):
        return f'Título: {self.titulo}\nAutor: {self.autor}\nPreço: {self.calcular_preco()}\nEstado: {self.estado}'

class Biblioteca:#crud -> gesta objetos
    def __init__(self):
        self.livros = []
    
    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'Livro {livro.titulo} adicionado')

    def listar_livros(self):
        if not self.livros:
            print('Biblioteca vazia')
        else:
            for livro in self.livros:
                print(f'{livro.exibir_informacao()}')
    
    def remover_livro (self, livro):
        if livro in self.livros:
            self.livros.remove(livro)
            print(f'Livro {livro.titulo} removido')
        else:
            print(f'Livro não encontrado')

    
biblioteca= Biblioteca()
livro01 = Livro('Brás Cubas', 'Machado', '100', 'semi-novo')
biblioteca.adicionar_livro(livro01)
biblioteca.listar_livros()
biblioteca.remover_livro(livro01)
biblioteca.listar_livros()
