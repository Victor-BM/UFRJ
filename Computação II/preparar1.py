class Usuário:
    def __init__ (self, nome, email, cpf):
        if (str.isalpha(nome)) and ('@' in email) and (str.isdigit(cpf) and len(cpf) == 11):
            self.nome = nome
            self.email = email
            self.__cpf = cpf
        else:
            print('Instanciação cancelada')
            return
    
    @property
    def cpf (self):
        return self.__cpf
    @cpf.setter
    def cpf (self, valor):
        self.__cpf = None
        if str.isdigit(valor) and len(valor) == 11:
            self.__cpf = valor
    def __str__ (self):
        return f'Nome: {self.nome}, Email: {self.email}'

class Aluno (Usuário):
    def __init__ (self, nome, email, cpf):
        Usuário.__init__(self, nome, email, cpf)
        self.estado_matrícula = 'ativa'
        self.cursos = []
    
    def inscrever_curso (self, curso):
        if self.estado_matrícula:
            self.cursos.append(curso)
            print(f'O aluno {self.nome} foi inscrito em {curso}')
    
    def ver_cursos (self):
        if len(self.cursos) != 0:
            print(f'O aluno {self.nome} está inscrito em:' + f'{self.cursos}')
        else:
            print(f'O aluno {self.nome} não está inscrito em nenhum curso')
    
    def __str__ (self):
        if len(self.cursos) == 0:
            cursos = 'Nenhum'
        else:
            cursos = self.cursos
        return f'Nome: {self.nome}, Email: {self.email}, Estado da matrícula: {self.estado_matrícula}, Cursos: {cursos}'
    
class Coordenador (Usuário):
    def __init__ (self, nome, email, cpf):
        Usuário.__init__(self, nome, email, cpf)
    
    def remover_curso (self, usuario, curso):
        if curso in usuario.cursos:
            usuario.cursos.remove(curso)
            print(f'O curso {curso} foi removido do aluno {usuario.nome}')
        else:
            print(f'O aluno {usuario.nome} não está inscrito em {curso}')
    
    def suspender_aluno (self, aluno):
        if aluno.estado_matrícula == 'ativa':
            aluno.estado_matrícula = 'suspensa'
            print(f'A matrícula de {aluno.nome} foi suspensa')
        else:
            aluno.estado_matrícula = 'ativa'
            print(f'A matrícula de {aluno.nome} foi ativada')
    def __str__ (self):
        return f'Coordenador: {self.nome}, Email: {self.email}'
    
aluno1 = Aluno ('Ana', 'ana@example.com', '12345678901')
coordenador1 = Coordenador ('Carlos', 'carlos@example.com', '98765432100')

aluno1.inscrever_curso('Matemática')
aluno1.ver_cursos()

coordenador1.remover_curso(aluno1, 'Matemática')
aluno1.ver_cursos()

coordenador1.suspender_aluno(aluno1)
print(aluno1)
print(coordenador1)

aluno1.remover_curso(aluno1, 'Matemática')