import pickle

class Livro:
    def __init__ (self, id, titulo, autor, ano, preco):
        try:
            self.id = id
            self.titulo = titulo
            self.autor = autor
            if ano.isdigit():
                self.ano = ano
            preco = float(preco)
            if preco > 0:
                self.preco = preco
            else:
                print('Erro ao instanciar o livro')
                return
        except:
            print('Erro ao instanciar o livro')
    
    def __str__ (self):
        return f'------------\nID: {self.id}\nTítulo: {self.titulo}\nAutor: {self.autor}\nAno: {self.ano}\nPreço: R${self.preco:.2f}\n------------'

class Estoque:
    def __init__(self):
        self.livros = []
        self.historico = []
    
    def adicionar_livro (self, livro):
        for livro_add in self.livros:
            if livro.id == livro_add.id:
                print(f'\nUm livro com ID {livro.id} já está presente no estoque')
                return
        self.livros.append(livro)
        print(f'\nO livro {livro.titulo} (ID: {livro.id}) foi adicionado ao estoque')
        self.historico.append(f'O livro {livro.titulo} (ID: {livro.id}) foi adicionado ao estoque')
        
    def remover_livro (self, id):
        tamanho = len(self.livros)
        for livro in self.livros:
            if livro.id == id:
                self.livros.remove(livro)
                print(f'\nO livro {livro.titulo} (ID: {livro.id}) foi removido do estoque')
                self.historico.append(f'O livro {livro.titulo} (ID: {livro.id}) foi removido do estoque')
        if len(self.livros) == tamanho:
            print(f'\nNão há nenhum livro com ID {id} presente no estoque')
    
    def listar_livros (self):
        print('\n')
        if len(self.livros) == 0:
            print('Estoque vazio')
        else:
            for livro in self.livros:
                print(livro.__str__())
    
    def salvar_estoque (self, arquivo):
        if len(self.livros) > 0:
            with open(arquivo, 'wb') as file:
                pickle.dump(self.livros, file)
            with open('historico.pkl', 'wb') as file:
                pickle.dump(self.historico, file)
            print(f'{arquivo} salvo com sucesso')
        else:
            print('Não foi possível salvar')

    def carregar_estoque (self, arquivo):
        try:
            with open(arquivo, 'rb') as file:
                self.livros = pickle.load(file)
            with open('historico.pkl', 'rb') as file:
                self.historico = pickle.load(file)
        except Exception as erro:
            print(f'Erro! {erro.__class__}')
    
    def pesquisar (self, pesquisa):
        pesquisa = pesquisa.lower()
        resultados = []
        for livro in self.livros:
            if pesquisa in livro.titulo.lower() or pesquisa in livro.autor.lower():
                resultados.append(livro.__str__())
        if len(resultados) == 0:
            print('\nNenhum livro encontrado')
        else:
            print('\nResultado da pesquisa:')
            for resultado in resultados:
                print (resultado)

def menu():
    print("\nMenu:")
    print("1. Adicionar Livro")
    print("2. Remover Livro")
    print("3. Listar Livros")
    print("4. Salvar Estoque")
    print("5. Carregar Estoque")
    print("6. Pesquisar livro por Título ou por Autor")
    print("7. Sair")
    return input("Escolha uma opção: ")

def main():
    estoque = Estoque()
    while True:
        opcao = menu()
        if opcao == '1':
            id = input("ID do Livro: ")
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            ano = input("Ano de Publicação: ")
            preco = float(input("Preço do Livro: "))
            livro = Livro(id, titulo, autor, ano, preco)
            estoque.adicionar_livro(livro)
        elif opcao == '2':
            id = input("ID do Livro a ser removido: ")
            estoque.remover_livro(id)
        elif opcao == '3':
            estoque.listar_livros()
        elif opcao == '4':
            nome_arquivo = input("Nome do arquivo para salvar o estoque: ")
            estoque.salvar_estoque(nome_arquivo)
        elif opcao == '5':
            nome_arquivo = input("Nome do arquivo para carregar o estoque: ")
            estoque.carregar_estoque(nome_arquivo)
        elif opcao == '6':
            pesquisa = input("Pesquisar: ")
            estoque.pesquisar(pesquisa)
        elif opcao == '7':
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()