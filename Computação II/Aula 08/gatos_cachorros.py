import abc, pickle

class Animal (abc.ABC):
    def __init__ (self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @abc.abstractmethod
    def fazer_som (self):
        pass

class Gato (Animal):
    def __init__(self, nome, idade, cor):
        Animal.__init__(self, nome, idade)
        self.cor =  cor
    
    def fazer_som(self):
        return('Miau!')

class Cachorro (Animal):
    def __init__(self, nome, idade, raça):
        Animal.__init__(self, nome, idade)
        self.raça =  raça
    
    def fazer_som(self):
        return('Au Au!')

class Crud:
    def __init__(self):
        self.animais = {}
    
    def cadastrar (self, nome, animal):
        if nome not in self.animais.keys(): 
            self.animais[nome] = animal
            print(f'{nome} cadastrado!')
        else:
            print(f'{nome} já cadastrado!')
    
    def excluir (self, nome):
        try:
            del self.animais[nome]
            print(f'{nome} excluído do cadastro!')
        except:
            print(f'{nome} não cadastrado!')
    
    def alterar_dados(self, nome, idade = None, caracteristica = None):
        if nome in self.animais:
            animal = self.animais[nome]
            if idade:
                animal.idade = idade
            if caracteristica:
                if isinstance(animal, Cachorro):
                    animal.raça = caracteristica
                if isinstance(animal, Gato):
                    animal.cor = caracteristica
            print (f'Informações de {nome} alteradas')
        else:
            print(f'{nome} não cadastrado')
    
    def listar (self):
        for nome, animal in self.animais.items():
            if isinstance(animal, Cachorro):
                print(f'{animal.__class__.__name__}: {nome}, Idade: {animal.idade}, Raça: {animal.raça}, Som: {animal.fazer_som()}')
            if isinstance(animal, Gato):
                print(f'{animal.__class__.__name__}: {nome}, Idade: {animal.idade}, Cor: {animal.cor}, Som: {animal.fazer_som()}')
    
    def salvar_dados (self, arquivo):
        with open (arquivo, 'wb') as file:
            pickle.dump(self.animais, file)
        print('Dados salvos com sucesso')
    
    def carregar_dados (self, arquivo):
        try:
            with open (arquivo, 'rb') as file:
                self.animais = pickle.load(file)
            print('Dados carregados com sucesso!')
        except FileNotFoundError:
            print('Arquivo não encontrado!')


Crud = Crud()
Crud.carregar_dados('animais.pkl')

def main():
    while True:
        print(f'\n\nMenu Principal\n1 - Cadastrar Animal\n2 - Listar Animais\n3 - Excluir Animal')
        print(f'4 - Alterar Animal\n5 - Sair\n\n')
        try:
            escolha = int(input('Digite uma opção: '))
        except:
            print('Opção inválida')
        else:
            if escolha == 1:
                print('1 - Cadastrar Cachorro\n2 - Cadastrar Gato')
                try:
                    cadastro = int(input('Digite uma opção de cadastro: '))
                    nome = input('Digite o nome: ')
                    idade = int(input('Digite a idade: '))
                except:
                    print('Opção inválida')
                else:
                    if cadastro == 1:
                        raça = input('Digite a raça: ')
                        animal01 = Cachorro(nome, idade, raça)
                    elif cadastro == 2:
                        cor = input('Digite a cor: ')
                        animal01 = Gato(nome, idade, cor)
                    else:
                        print('Opção inválida')
                        return
                    Crud.cadastrar(nome, animal01)
            elif escolha == 2:
                Crud.listar()
            elif escolha == 3:
                nome = input('Digite o nome do animal a ser removido: ')
                Crud.excluir(nome)
            elif escolha == 4:
                print('1 - Alterar Cachorro\n2 - Alterar Gato')
                try:
                    alterar = int(input('Digite uma opção de alteração: '))
                    nome = input('Digite o nome do animal a ser alterado: ')
                except:
                    print('Opção inválida')
                else:
                    idade = input('Nova idade (Enter para manter): ')
                    if idade.isdigit():
                        idade = int(idade)
                    elif idade != None and not isinstance (idade, int):
                        idade = None
                    if alterar == 1:
                        raça = input('Nova raça (Enter para manter): ')
                        Crud.alterar_dados(nome, idade, raça)
                    elif alterar == 2:
                        cor = input('Nova cor (Enter para manter): ')
                        Crud.alterar_dados(nome, idade, cor)
                    else:
                        print('Opção inválida')
                        return
            elif escolha == 5:
                print('Encerrando programa')
                Crud.salvar_dados('animais.pkl')
                break
            else:
                print('Opção inválida')
main()