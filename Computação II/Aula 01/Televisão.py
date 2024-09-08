class Televisão:
    def __init__(self, polegadas, marca, preço):
        self.polegadas = int(polegadas)
        self.marca = marca
        self.preço = float(preço)
        self.estado = False
        self.canal = 1
        self.volume = 1
    
    def ligar(self):
        if self.estado == False:
            self.estado = True
            print('A TV foi ligada')
        else:
            self.estado == False
            print('A TV foi desligada')
    
    def verificar_estado(self):
        return 'Ligada' if self.estado else 'Desligada'
    
    def mudar_canal(self, novo_canal):
        if self.estado:
            if 1 <= novo_canal < 5000:
                self.canal = novo_canal
                print(f'Canal alterado para: {self.canal}')
            else:
                print('Canal inválido!')
        else:
            self.canal = 1
            print('A TV está desligada! Ligue-a!')

    def mudar_volume(self, novo_volume):
        if self.estado:
            if 1<= novo_volume < 80:
                self.volume = novo_volume
                print(f'Volume alterado para: {self.volume}')
            elif 80 <= novo_volume < 100:
                resposta = input('Volume alto, deseja continuar? [S ou N] ').lower()
                if resposta == 's':
                    self.volume = novo_volume
                    print(f'Volume alterado para: {self.volume}')
                else:
                    self.volume = 79
                    print('Volume ajustado para: 79')
            else:
                print('Volume inválido')
        else:
            print('A TV está desligada! Ligue-a!')
    
    def ficha(self):
        Estado = self.verificar_estado()
        alerta = 'Volume Alto' if self.volume >= 80 else 'Volume Normal'
        print(f'Marca: {self.marca}\nEstado: {Estado}\nVolume: {self.volume} - {alerta}\nCanal: {self.canal}')

tv01 = Televisão('50', 'Samsung', '1850')
tv01.ligar()
tv01.mudar_canal (743)
tv01.mudar_volume(97)
tv01.ficha()