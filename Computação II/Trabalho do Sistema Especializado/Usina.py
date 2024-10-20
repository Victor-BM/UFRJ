import abc
import random

elementos_radioativos = ['U-238', 'Pu-239', 'Se-79', 'Zr-93', 'Te-99', 'Pd-107', 'Sn-126', 'I-129', 'Cs-135', 'Sr-89', 'Sr-90', 'Ru-106', 'Sn-125', 'Cs-134', 'Cs-137', 'Pm-147', 'I-131']
porcentagem_geracao = [93, 1.3, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, 0.38, ]

class Usuário (abc.ABC):
  def __init__ (self, nome:str, idade:int, salario:float, id:str):
    self.nome = nome
    self.idade = idade
    self.__salario = salario
    self.id = id

  @property
  def salário (self):
    return self.__salario
  
  @abc.abstractmethod
  def __str__ (self):
     pass

class Técnico (Usuário):
  def __init__ (self, nome:str, idade:int, salario:float, id:int, atuação:str):
    Usuário.__init__ (self, nome, idade, salario, id)
    self.atuação = atuação
    
  def __str__ (self):
    return f'Técnico: {self.nome}, Idade: {self.idade}, Salário: {self.salário}, Id: {self.id}, Atuação: {self.atuação}'

class Engenheiro (Usuário):
  def __init__ (self, nome:str, idade:int, salario:float, id:int, especialidade:str):
    Usuário.__init__ (self, nome, idade, salario, id)
    self.especialidade = especialidade
    
  def __str__ (self):
    return f'Engenheiro: {self.nome}, Idade: {self.idade}, Salário: {self.salário}, Id: {self.id}, Especialidade: {self.especialidade}'
   
class Supervisor (Usuário):
  def __init__ (self, nome:str, idade:int, salario:float, id:int):
    Usuário.__init__ (self, nome, idade, salario, id)
    
  def __str__ (self):
    return f'Supervisor: {self.nome}, Idade: {self.idade}, Salário: {self.salário}, Id: {self.id}'

class Usina:
  def __init__ (self, capacidade: float):
    self.capacidade = capacidade
    self.__desgaste = 0
    self.__eficiencia = 0.2
    self.__residuos = []
    self.estado = False
    self.producao = 0
    self.__sistema_automacao = None
    self.__nivel_automacao = None
    self.__metodologia = None

  @property
  def eficiencia (self):
    return self.__eficiencia

  @property
  def desgaste (self):
    return self.__desgaste

  @property
  def residuos (self):
    return self.__residuos
  
  @property
  def metodologia (self):
    return self.__metodologia
  
  @property
  def sistema_automacao(self):
    return self.__sistema_automacao

  @property
  def nivel_automacao(self):
    return self.__nivel_automacao

  def input_valido(self, prompt, opcoes_validas):
    while True:
      escolha = input(prompt)
      if escolha == "0":  # Verifica se é a string '0' para cancelar
        return 0
      if escolha.isdigit() and int(escolha) in opcoes_validas:
        return int(escolha)
      else:
        print("Opção inválida. Tente novamente.")

  def calcular_producao (self):
    self.producao = self.capacidade*self.eficiencia
    return self.producao

  def gerar_energia (self, usuario):
    if isinstance(usuario, Supervisor):
      print('Acesso autorizado!')
      if self.desgaste == 100:
        print('Desgaste máximo atingido, não foi possível ligar a usina!')
      elif len(self.residuos) == 10:
        print('A usina está repleta de resíduos, não foi possível ligá-la')
      elif self.desgaste < 100 and len(self.residuos) < 10:
        self.estado = True
        print('A usina está gerando energia!')
        self.__desgaste += 10
        self.__residuos.append(random.choices(elementos_radioativos, weights = porcentagem_geracao, k =1)[0])
        self.__eficiencia -= 0.03
        if self.eficiencia < 0:
          self.__eficiencia = 0
        print('Energia gerada! Encerrando operações.')
        print(f'Status Atual\nDesgate: {self.desgaste}%\nResíduos acumulados: {self.residuos}\nEficiência: {self.eficiencia:.2f}')
        self.estado = False
    else:
      print('Acesso negado!')

  def otimizar(self, usuario):
    if isinstance(usuario, Supervisor):
        print("Escolha com qual metodologia será otimizada a usina:\n"
              "0 - Cancelar Operação\n"
              "1 - Lean Manufacturing (+0.15 eficiência)\n"
              "2 - Six Sigma (+0.10 eficiência)\n"
              "3 - Kaizen (+0.12 eficiência)\n"
              "4 - 5S (+0.07 eficiência)\n"
              "5 - Total Productive Maintenance (TPM) (+0.20 eficiência)")

        escolha = self.input_valido("Digite o número da metodologia escolhida: ", [1, 2, 3, 4, 5])

        if escolha == 0:
           print('Operação cancelada')
           return
        if escolha == 1:
            self.__eficiencia += 0.15
            self.__metodologia = "Lean Manufacturing"
        elif escolha == 2:
            self.__eficiencia += 0.10
            self.__metodologia = "Six Sigma"
        elif escolha == 3:
            self.__eficiencia += 0.12
            self.__metodologia = "Kaizen"
        elif escolha == 4:
            self.__eficiencia += 0.07
            self.__metodologia = "5S"
        elif escolha == 5:
            self.__eficiencia += 0.20
            self.__metodologia = "Total Productive Maintenance (TPM)"

        if self.__eficiencia > 1.0:
            self.__eficiencia = 1.0

        print(f"Supervisor {usuario.nome} aplicou {self.metodologia}. Eficiência aumentada para {self.__eficiencia:.2f}.")
    else:
        print(f"{usuario.nome} não tem permissão para otimizar a usina.")

  def manutencao (self, usuario):
    if isinstance(usuario, Técnico):
      if not self.estado:
        if self.desgaste != 0:
          self.__desgaste -= 10
          if self.desgaste < 0:
            self.__desgaste = 0
          print(f'Manutenção realizada!\nO desgaste agora é de: {self.desgaste}%')
        else:
          print('Todos os equipamentos estão com manutenção em dia!')
      else:
        print('É necessário encerrar operações para realizar uma manutenção segura!')
    else:
      print('Acesso negado!')

  def calcular_eficiencia_automacao(self, usuario):
    if isinstance(usuario, (Engenheiro, Técnico)):
        print("Escolha o sistema de automação para configurar a usina:\n"
              "0 - Cancelar Operação\n"
              "1 - PLC (+0.05 eficiência)\n"
              "2 - SCADA (+0.10 eficiência)\n"
              "3 - DCS (+0.12 eficiência)\n"
              "4 - HMI (+0.16 eficiência)\n"
              "5 - IoT (+0.20 eficiência)")

        escolha_sistema = self.input_valido("Digite o número do sistema de automação escolhido: ", [1, 2, 3, 4, 5])

        if escolha_sistema == 0:
           print('Operação cancelada')
           return
        elif escolha_sistema == 1:
            incremento_sistema = 0.05
            self.__sistema_automacao = "PLC"
        elif escolha_sistema == 2:
            incremento_sistema = 0.10
            self.__sistema_automacao = "SCADA"
        elif escolha_sistema == 3:
            incremento_sistema = 0.12
            self.__sistema_automacao = "DCS"
        elif escolha_sistema == 4:
            incremento_sistema = 0.16
            self.__sistema_automacao = "HMI"
        elif escolha_sistema == 5:
            incremento_sistema = 0.20
            self.__sistema_automacao = "IoT"

        print("Escolha o nível de automação:\n"
              "0 - Cancelar Operação\n"
              "1 - Muito Baixo (1.0x)\n"
              "2 - Baixo (1.1x)\n"
              "3 - Médio (1.4x)\n"
              "4 - Alto (1.7x)\n"
              "5 - Muito Alto (2.0x)")

        escolha_nivel = self.input_valido("Digite o número do nível de automação escolhido: ", [1, 2, 3, 4, 5])
        
        if escolha_nivel == 0:
           print('Operação cancelada')
           return
        elif escolha_nivel == 1:
            multiplicador_nivel = 1.0
            self.__nivel_automacao = "Muito Baixo"
        elif escolha_nivel == 2:
            multiplicador_nivel = 1.1
            self.__nivel_automacao = "Baixo"
        elif escolha_nivel == 3:
            multiplicador_nivel = 1.4
            self.__nivel_automacao = "Médio"
        elif escolha_nivel == 4:
            multiplicador_nivel = 1.7
            self.__nivel_automacao = "Alto"
        elif escolha_nivel == 5:
            multiplicador_nivel = 2.0
            self.__nivel_automacao = "Muito Alto"

        incremento = incremento_sistema * multiplicador_nivel
        self.__eficiencia += incremento

        if self.__eficiencia > 1.0:
            self.__eficiencia = 1.0

        print(f"{usuario.__class__.__name__} {usuario.nome} configurou a usina com o sistema {self.sistema_automacao} e automação {self.nivel_automacao}.")
        print(f"Eficiência aumentada para {self.__eficiencia:.2f}.")
    else:
        print(f"{usuario.nome} não tem permissão para configurar a automação da usina.")

  def gestao_residuos (self, usuario):
    if isinstance(usuario, Engenheiro):
      if not self.estado:
        quantidade_residuos = len(self.residuos)
        if quantidade_residuos != 0:
          self.__residuos.remove(self.residuos[quantidade_residuos - 1])
          quantidade_residuos = len(self.residuos)
          print(f'Gestão de resíduos realizada!\nA quantidade de resíduos presente agora é de: {quantidade_residuos} itens')
        else:
          print('A gestão de resíduos está em dia!')
      else:
        print('É necessário encerrar operações para realizar uma gestão de resíduos segura!')
    else:
      print('Acesso negado!')

  def ficha(self):
      self.producao = self.calcular_producao()
      ficha = f"""
      Ficha Técnica da Usina:
      -------------------------
      Capacidade: {self.capacidade} GWh
      Desgaste: {self.desgaste}%
      Eficiência: {self.eficiencia:.2f}
      Produção: {self.producao:.2f} GWh
      Quantidade de Resíduos Acumulados: {len(self.residuos)} itens
      Resíduos Acumulados: {(self.residuos)}
      Sistema de Automação: {self.sistema_automacao if self.sistema_automacao else "Não configurado"}
      Nível de Automação: {self.nivel_automacao if self.nivel_automacao else "Não configurado"}
      Otimização: {self.metodologia if self.metodologia else "Não configurada"}
      -------------------------
      """
      print(ficha)

Usina01 = Usina(1000)
supervisor01 = Supervisor('Ana', 35, 15000, '001')
engenheiro01 = Engenheiro('João', 25, 10000, '002', 'Nuclear')
tecnico01 = Técnico('José', 50, 7500, '003', 'Mecânica')
Usina01.gerar_energia(engenheiro01)
Usina01.gerar_energia(supervisor01)
Usina01.gerar_energia(supervisor01)
Usina01.manutencao(tecnico01)
Usina01.gestao_residuos(engenheiro01)
Usina01.otimizar(supervisor01)
Usina01.calcular_eficiencia_automacao(engenheiro01)
Usina01.gerar_energia(supervisor01)
Usina01.gerar_energia(supervisor01)
Usina01.gerar_energia(supervisor01)
Usina01.ficha()