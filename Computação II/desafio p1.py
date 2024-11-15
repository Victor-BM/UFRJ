class Usuario:
    def __init__ (self, nome, email, cpf):
        if str.isalpha(nome):
            self.nome = nome
        if '@' in email:
            self.email = email
        if str.isdigit(cpf):
            self.__cpf = cpf
    
    @property
    def cpf (self):
        return self.__cpf
    
    @cpf.setter
    def cpf (self, valor):
        if str.isdigit(valor):
            self.__cpf = valor
        else:
            self.__cpf = None
    
    def __str__ (self):
        return f'\nNome: {self.nome}, Email: {self.email}'    
        
    
    
class Aluno (Usuario):
    def __init__ (self, nome, email, cpf):
        Usuario.__init__(self, nome, email, cpf)
        self.cursos = []
        self.estado_matricula = 'ativa'

    def inscrever_curso (self, curso):
        if self.estado_matricula != 'suspensa':
            self.cursos.append(curso)
            print(f'\nO aluno {self.nome} foi inscrito em {curso}')
        else:
            print('\nMatrícula suspensa')
        
    def ver_cursos (self):
        if len(self.cursos) != 0:
            print(f'\nCursos inscritos de {self.nome}:')
            for element in self.cursos:
                print(element)
        else:
            print(f'\nO aluno {self.nome} não está inscrito em nenhum curso')
    
    def __str__ (self):
        if len(self.cursos) == 0:
            cursos = 'Nenhum'
        else:
            cursos = self.cursos
        return f'\nNome: {self.nome}, Email: {self.email}, Estado de matrícula: {self.estado_matricula}, Cursos: {cursos}'
    
class Coordenador (Usuario):
    def __init__ (self, nome, email, cpf):
        Usuario.__init__(self, nome, email, cpf)
        
    def remover_curso (self, usuario, curso):
        usuario.cursos.remove(curso)
        print(f'\nO curso {curso} removido de {usuario.nome}')
    
    def suspender_aluno (self, aluno):
        if aluno.estado_matricula == 'suspensa':
            aluno.estado_matricula = 'ativa'
        else:
            aluno.estado_matricula = 'suspensa'
        print(f'\nEstado da matrícula de {aluno.nome}: {aluno.estado_matricula}')
        
    def __str__ (self):
        return(f'\nCoordenador: {self.nome}, Email: {self.email}')
    

aluno1 = Aluno('Ana', 'ana@exemple.com', '12345678901')
coordenador1 = Coordenador('Carlos', 'carlos@exemple.com', '98765432100')
aluno1.inscrever_curso('Matemática')
aluno1.ver_cursos()
coordenador1.remover_curso(aluno1, 'Matemática')
aluno1.ver_cursos()
coordenador1.suspender_aluno(aluno1)
print(aluno1)
print(coordenador1)
aluno1.remover_curso(aluno1, 'Matemática')