class DragQueen:
    def __init__ (self, nome, out_of_drag, haus = ''):
        self.nome = nome
        self.out_of_drag = out_of_drag
        self.haus = haus
    
    def __str__(self):
        if self.haus != '':
            return f'INHAIIIIIII, aqui é a {self.__class__.__name__} {self.nome}. Da haus {self.haus}'
        else:
            return f'INHAIIIIIII, aqui é a {self.__class__.__name__} {self.nome}.'

    def maquiar(self):
        print('Se maquiando.')
    
    def lipsync (self, música):
        print(f'Fazendo um lipsync de {música}')
        
class Performer (DragQueen):
    def __init__(self, nome, out_of_drag, haus = '', repertório = ''):
        DragQueen.__init__(self, nome, out_of_drag, haus)
        self.repertório = repertório
    
    def performar (self):
        print(f'Performando a sua especialidade, {self.repertório}')

class Artísitica (DragQueen):
    def __init__(self, nome, out_of_drag, haus = '' , material_preferido = ''):
        super().__init__(nome, out_of_drag, haus)
        self.material_preferido = material_preferido
    
    def apresentarMaterial (self):
        print(f'Mostrando sua aptidão artística com {self.material_preferido}')

class CUNT (Performer, Artísitica):
    def __init__(self, nome, out_of_drag, haus = '', repertório = '', material_preferido = ''):
        Performer.__init__(self, nome, out_of_drag, haus, repertório)
        Artísitica.__init__(self, nome, out_of_drag, haus, material_preferido)

drag1 = DragQueen("Wilma Cobra", "Adenílson Silva")
drag1.maquiar()
drag1.lipsync("Erva Venenosa, Rita Lee")
print(drag1)
print('\n\n')
performer1 = Performer("Mama Deira", "Natasha Costa", "Deiras", "Contorcionismo")
performer1.performar()
print(performer1)
print('\n\n')
artistica1 = Artísitica("Kidoi Deira", "Marcos Pereira", "Deiras", "Maquiagem animalesca")
artistica1.apresentarMaterial()
print(artistica1)
print('\n\n')
cunt1 = CUNT("Dina Mitada", "Thiago Sousa", '', "Acrobacias", "Pedrarias")
cunt1.performar()
cunt1.apresentarMaterial()
print(cunt1)