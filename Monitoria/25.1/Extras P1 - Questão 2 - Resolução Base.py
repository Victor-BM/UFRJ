from abc import ABC, abstractmethod

class CorpoCeleste(ABC):
    def __init__(self, nome, massa):
        try:
            if not isinstance(nome, str) or not nome.strip():
                raise ValueError("O nome não pode estar vazio.")
            if not isinstance(massa, (int, float)) or massa <= 0:
                raise ValueError("A massa deve ser positiva.")
            self.nome = nome
            self.massa = massa
        except ValueError as e:
            print(f"Erro ao criar corpo celeste: {e}")
            self.nome = ""
            self.massa = 0.0

    @abstractmethod
    def exibir_info(self):
        pass

class Planeta(CorpoCeleste):
    def __init__(self, nome, massa, diametro):
        super().__init__(nome, massa)
        try:
            if not isinstance(diametro, (int, float)) or diametro <= 0:
                raise ValueError("O diâmetro deve ser positivo.")
            self.diametro = diametro
        except ValueError as e:
            print(f"Erro ao criar planeta: {e}")
            self.diametro = 0.0

    def exibir_info(self):
        return f"Nome: {self.nome}, Massa: {self.massa} kg, Diâmetro: {self.diametro} km"

    def orbitar(self, corpo):
        if isinstance(corpo, CorpoCeleste):
            return f"{self.nome} orbitando {corpo.nome}."
        else:
            return f"{self.nome} não pode orbitar um objeto que não é um Corpo Celeste."

class Estelar(CorpoCeleste, ABC):
    def __init__(self, nome, massa, luminosidade):
        super().__init__(nome, massa)
        try:
            if not isinstance(luminosidade, (int, float)) or luminosidade <= 0:
                raise ValueError("A luminosidade deve ser positiva.")
            self.luminosidade = luminosidade
        except ValueError as e:
            print(f"Erro ao criar corpo estelar: {e}")
            self.luminosidade = 0.0

    @abstractmethod
    def emitir_luz(self):
        pass

class Estrela(Estelar):
    def __init__(self, nome, massa, luminosidade, tipo_espectral):
        super().__init__(nome, massa, luminosidade)
        try:
            if not isinstance(tipo_espectral, str) or not tipo_espectral.strip():
                raise ValueError("O tipo espectral não pode ser vazio.")
            self.tipo_espectral = tipo_espectral
        except ValueError as e:
            print(f"Erro ao criar estrela: {e}")
            self.tipo_espectral = ""

    def exibir_info(self):
        return f"Nome: {self.nome}, Massa: {self.massa} kg, Luminosidade: {self.luminosidade} W, Tipo Espectral: {self.tipo_espectral}"

    def emitir_luz(self):
        return f"{self.nome} emitindo luz."

class Supernova(Estelar):
    def __init__(self, nome, massa, luminosidade, magnitude_absoluta):
        super().__init__(nome, massa, luminosidade)
        self.magnitude_absoluta = magnitude_absoluta

    def exibir_info(self):
        return f"Nome: {self.nome}, Massa: {self.massa} kg, Luminosidade: {self.luminosidade} W, Magnitude Absoluta: {self.magnitude_absoluta}"

    def emitir_luz(self):
        return f"{self.nome} emitindo luz intensamente."

    def colapsar(self):
        return f"{self.nome} colapsou."

class BuracoNegro(CorpoCeleste):
    def __init__(self, nome, massa, raio_schwarzschild):
        super().__init__(nome, massa)
        try:
            if not isinstance(raio_schwarzschild, (int, float)) or raio_schwarzschild <= 0:
                raise ValueError("O raio de Schwarzschild deve ser positivo.")
            self.raio_schwarzschild = raio_schwarzschild
        except ValueError as e:
            print(f"Erro ao criar buraco negro: {e}")
            self.raio_schwarzschild = 0.0

    def exibir_info(self):
        return f"Nome: {self.nome}, Massa: {self.massa} kg, Raio de Schwarzschild: {self.raio_schwarzschild} m"

class Orbitavel(ABC):
    @abstractmethod
    def orbitar(self, corpo):
        pass

class SateliteNatural(CorpoCeleste, Orbitavel):
    def __init__(self, nome, massa, corpo_orbitado):
        super().__init__(nome, massa)
        try:
            if not isinstance(corpo_orbitado, str) or not corpo_orbitado.strip():
                raise ValueError("O corpo orbitado não pode estar vazio.")
            self.corpo_orbitado = corpo_orbitado
        except ValueError as e:
            print(f"Erro ao criar satélite: {e}")
            self.corpo_orbitado = ""

    def exibir_info(self):
        return f"Nome: {self.nome}, Massa: {self.massa} kg, Orbitando: {self.corpo_orbitado}"

    def orbitar(self, corpo):
        if isinstance(corpo, CorpoCeleste):
            return f"{self.nome} orbitando {corpo.nome}."
        else:
            return f"{self.nome} não pode orbitar um objeto que não é um Corpo Celeste."

class Cometa(CorpoCeleste, Orbitavel):
    def __init__(self, nome, massa, periodo_orbital):
        super().__init__(nome, massa)
        try:
            if not isinstance(periodo_orbital, (int, float)) or periodo_orbital <= 0:
                raise ValueError("O período orbital deve ser positivo.")
            self.periodo_orbital = periodo_orbital
        except ValueError as e:
            print(f"Erro ao criar cometa: {e}")
            self.periodo_orbital = 0.0

    def exibir_info(self):
        return f"Nome: {self.nome}, Massa: {self.massa} kg, Período Orbital: {self.periodo_orbital} anos"

    def orbitar(self, corpo):
        if isinstance(corpo, CorpoCeleste):
            return f"{self.nome} orbitando {corpo.nome} com um período de {self.periodo_orbital} anos."
        else:
            return f"{self.nome} não pode orbitar um objeto que não é um Corpo Celeste."

def simular_acao_celeste(corpo):
    print(f"--- Informações e Simulação ---")
    print(corpo.exibir_info())
    if isinstance(corpo, Orbitavel):
        if hasattr(corpo, 'orbita'):
            print(corpo.orbitar(corpo.orbita))
        
    if isinstance(corpo, Estelar):
        print(corpo.emitir_luz())
        if isinstance(corpo, Supernova):
            print(corpo.colapsar())

if __name__ == "__main__":
    print("Criando corpos celestes...")
    terra = Planeta("Terra", 5.972e+24, 12742.0)
    sol = Estrela("Sol", 1.989e+30, 3.828e+26, "G2V")
    sn1987a = Supernova("SN 1987A", 3.0e+31, 1.0e+39, -16.0)
    cygnus_x1 = BuracoNegro("Cygnus X-1", 3.0e+31, 8850.0)
    lua = SateliteNatural("Lua", 7.3476e+22, "Terra")
    halley = Cometa("Halley", 2.2e+14, 76.0)
    planeta_invalido = Planeta("Y", 1.0e+25, -100.0)
    estrela_invalida = Estrela("Z", 1.0e+30, 1.0e+26, "")
    buraco_negro_invalido = BuracoNegro("W", 1.0e+32, -5000.0)
    satelite_invalido = SateliteNatural("M", 1.0e+22, "")
    cometa_invalido = Cometa("C", 1.0e+15, -10.0)
    estrela_invalida_lum = Estrela("V", 1.0e+30, -1.0e+26, "A0")
    supernova_invalida_lum = Supernova("S", 5.0e+31, -2.0e+39, -18.0)

    corpos_celestes = [terra, sol, sn1987a, cygnus_x1, lua, halley]

    print("\n--- Informações e Simulação ---")
    for corpo in corpos_celestes:
        simular_acao_celeste(corpo)