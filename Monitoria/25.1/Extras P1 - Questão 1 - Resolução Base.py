from abc import ABC, abstractmethod

class EstoqueVazioError(Exception):
    """Exceção levantada quando o estoque está vazio."""
    pass

class GraoNaoEncontradoError(Exception):
    """Exceção levantada quando um grão não é encontrado no estoque."""
    pass

class Grao(ABC):
    def __init__(self, nome, lote, quantidade):
        try:
            self._validar_dados(nome, lote, quantidade)
            self._nome = nome
            self._lote = lote
            self._quantidade = quantidade
        except ValueError as e:
            print(f"Erro ao criar grão: {e}")
            self._nome = ""
            self._lote = ""
            self._quantidade = 0

    def _validar_dados(self, nome, lote, quantidade):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome não pode estar vazio.")
        if not isinstance(lote, str) or not lote.strip():
            raise ValueError("O lote não pode estar vazio.")
        if not isinstance(quantidade, (int, float)) or quantidade < 0:
            raise ValueError("A quantidade não pode ser negativa.")

    def get_nome(self):
        return self._nome

    def get_lote(self):
        return self._lote

    def get_quantidade(self):
        return self._quantidade

    def set_quantidade(self, nova_quantidade):
        try:
            if not isinstance(nova_quantidade, (int, float)) or nova_quantidade < 0:
                raise ValueError("A quantidade não pode ser negativa.")
            self._quantidade = nova_quantidade
            return True
        except ValueError as e:
            print(f"Erro ao definir quantidade para {self._nome} ({self._lote}): {e}")
            return False

    @abstractmethod
    def classificar_qualidade(self):
        pass

    def exibir_info(self):
        print(f"Nome: {self._nome}, Lote: {self._lote}, Quantidade: {self._quantidade} kg", end="")

class Milho(Grao):
    def __init__(self, nome, lote, quantidade, umidade):
        super().__init__(nome, lote, quantidade)
        try:
            self._validar_umidade(umidade)
            self._umidade = umidade
        except ValueError as e:
            print(f"Erro ao criar grão Milho: {e}")
            self._umidade = None

    def _validar_umidade(self, umidade):
        if not isinstance(umidade, float) or not 0 <= umidade <= 1:
            raise ValueError("A umidade deve estar entre 0 e 1.")

    def classificar_qualidade(self):
        if self._umidade is not None:
            if self._umidade < 0.1:
                return "Bom"
            elif 0.1 <= self._umidade <= 0.15:
                return "Regular"
            else:
                return "Ruim"
        return "N/A"

    def exibir_info(self):
        super().exibir_info()
        if self._umidade is not None:
            print(f", Umidade: {self._umidade:.2f}, Qualidade: {self.classificar_qualidade()}")
        else:
            print(", Umidade: N/A, Qualidade: N/A")

class Soja(Grao):
    def __init__(self, nome, lote, quantidade, teor_proteina):
        super().__init__(nome, lote, quantidade)
        try:
            self._validar_teor_proteina(teor_proteina)
            self._teor_proteina = teor_proteina
        except ValueError as e:
            print(f"Erro ao criar grão Soja: {e}")
            self._teor_proteina = None

    def _validar_teor_proteina(self, teor_proteina):
        if not isinstance(teor_proteina, float) or teor_proteina <= 0:
            raise ValueError("O teor de proteína deve ser positivo.")

    def classificar_qualidade(self):
        if self._teor_proteina is not None:
            if self._teor_proteina > 0.4:
                return "Alto"
            elif 0.3 <= self._teor_proteina <= 0.4:
                return "Médio"
            else:
                return "Baixo"
        return "N/A"

    def exibir_info(self):
        super().exibir_info()
        if self._teor_proteina is not None:
            print(f", Teor de Proteína: {self._teor_proteina:.2f}, Qualidade: {self.classificar_qualidade()}")
        else:
            print(", Teor de Proteína: N/A, Qualidade: N/A")

class Trigo(Grao):
    def __init__(self, nome, lote, quantidade, tipo):
        super().__init__(nome, lote, quantidade)
        try:
            self._validar_tipo(tipo)
            self._tipo = tipo
        except ValueError as e:
            print(f"Erro ao criar grão Trigo: {e}")
            self._tipo = None

    def _validar_tipo(self, tipo):
        if not isinstance(tipo, str) or not tipo.strip():
            raise ValueError("O tipo não pode estar vazio.")

    def classificar_qualidade(self):
        return self._tipo if self._tipo is not None else "N/A"

    def exibir_info(self):
        super().exibir_info()
        if self._tipo:
            print(f", Tipo: {self._tipo}, Qualidade: {self.classificar_qualidade()}")
        else:
            print(", Tipo: N/A, Qualidade: N/A")

class ArmazemDeGraos:
    def __init__(self):
        self._estoque = {}

    def adicionar_grao(self, grao):
        if isinstance(grao, Grao) and grao.get_nome() and grao.get_lote():
            if grao.get_lote() in self._estoque:
                print(f"Aviso: Já existe um grão com o lote '{grao.get_lote()}'.")
            self._estoque[grao.get_lote()] = grao
            return True
        else:
            print("Erro ao adicionar grão: Objeto inválido ou com dados essenciais ausentes.")
            return False

    def visualizar_estoque(self):
        try:
            if not self._estoque:
                raise EstoqueVazioError("O estoque de grãos está vazio.")
            print("--- Estoque Atual ---")
            for grao in self._estoque.values():
                grao.exibir_info()
            return True
        except EstoqueVazioError as e:
            print(f"Erro ao visualizar estoque: {e}")
            return False

    def buscar_grao(self, lote):
        if not isinstance(lote, str) or not lote.strip():
            print("Erro ao buscar grão: O lote para busca não pode estar vazio.")
            return None
        return self._estoque.get(lote)

    def atualizar_quantidade(self, lote, nova_quantidade):
        if not isinstance(lote, str) or not lote.strip():
            print("Erro ao atualizar quantidade: O lote para atualização não pode estar vazio.")
            return False
        grao = self.buscar_grao(lote)
        try:
            if grao:
                return grao.set_quantidade(nova_quantidade)
            else:
                raise GraoNaoEncontradoError(f"Grão com lote '{lote}' não encontrado no estoque.")
        except GraoNaoEncontradoError as e:
            print(f"Erro ao atualizar quantidade: {e}")
            return False

    def remover_grao(self, lote):
        if not isinstance(lote, str) or not lote.strip():
            print("Erro ao remover grão: O lote para remoção não pode estar vazio.")
            return False
        try:
            if lote in self._estoque:
                del self._estoque[lote]
                print("Grão removido com sucesso.")
                return True
            else:
                raise GraoNaoEncontradoError(f"Grão com lote '{lote}' não encontrado no estoque.")
        except GraoNaoEncontradoError as e:
            print(f"Erro ao remover grão: {e}")
            return False
        
# Bloco principal do seu código (simplificado)
if __name__ == "__main__":
    armazem = ArmazemDeGraos()

    print("Adicionando grãos ao armazém...")
    armazem.adicionar_grao(Milho("Milho Variedade A", "2025-M1", 150.0, 0.08))
    armazem.adicionar_grao(Soja("Soja Orgânica", "2025-S1", 200.0, 0.42))
    armazem.adicionar_grao(Trigo("Trigo Comum", "2025-T1", 300.0, "Mole"))
    armazem.adicionar_grao(Milho("", "2025-M2", 100.0, 0.12))
    armazem.adicionar_grao(Soja("Soja Transgênica", "", 180.0, 0.35))
    armazem.adicionar_grao(Trigo("Trigo Integral", "2025-T2", -50.0, "Duro"))
    armazem.adicionar_grao(Milho("Milho Pipoca", "2025-M3", 120.0, 1.2))
    armazem.adicionar_grao(Soja("Soja Especial", "2025-S2", 250.0, -0.1))
    armazem.adicionar_grao(Trigo("Trigo Sarraceno", "2025-T3", 400.0, ""))

    print("\n--- Estoque Inicial ---")
    armazem.visualizar_estoque()

    print("\nBuscando grão com lote 2025-S1...")
    grao_encontrado = armazem.buscar_grao("2025-S1")
    if grao_encontrado:
        print("Grão encontrado:", end=" ")
        grao_encontrado.exibir_info()
    else:
        print("Grão não encontrado.")

    print("\nAtualizando quantidade do lote 2025-M1 para 180.0 kg...")
    armazem.atualizar_quantidade("2025-M1", 180.0)

    print("\n--- Estoque Após Atualização ---")
    armazem.visualizar_estoque()

    print("\nRemovendo grão com lote 2025-T1...")
    armazem.remover_grao("2025-T1")

    print("\n--- Estoque Final ---")
    armazem.visualizar_estoque()

    print("\nTentando remover grão inexistente...")
    armazem.remover_grao("2025-X1")

    print("\nTentando visualizar estoque vazio...")
    armazem_vazio = ArmazemDeGraos()
    armazem_vazio.visualizar_estoque()