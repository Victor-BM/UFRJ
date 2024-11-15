lista_funcionarios = []
lista_salarios = []
lista_funcionarios_atualizada = []

def criar_arquivo_funcionarios():
    funcionarios = []
    try:
        quantidade = int(input('Quantos funcionários você deseja cadastrar? '))
    except Exception as erro:
        print(f'{erro.__class__}')
    else:
        if quantidade > 0:
            for num in range(quantidade):
                print(f'\nFuncionário número {num + 1}')
                id = input(f'Qual o id? ')
                nome = input(f'Qual o nome? ')
                cargo = input(f'Qual o cargo? ')
                if id.isdigit() and nome.isalpha() and cargo.isalpha():
                    funcionarios.append([id, nome, cargo])
                else:
                    print('Erro de instanciação!')
        else:
            print('Quantidade inválida')
    with open ('funcionarios.txt', 'w', encoding = 'utf-8') as file:
        for i in range(len(funcionarios)):
            if i < (len(funcionarios) - 1):
                file.write(f'{funcionarios[i][0]}, {funcionarios[i][1]}, {funcionarios[i][2]}\n')
            else:
                file.write(f'{funcionarios[i][0]}, {funcionarios[i][1]}, {funcionarios[i][2]}')

def criar_arquivo_salarios():
    salarios = []
    try:
        quantidade = int(input('Quantos salários você deseja cadastrar? '))
    except Exception as erro:
        print(f'{erro.__class__}')
    else:
        if quantidade > 0:
            for num in range(quantidade):
                print(f'\nDado número {num + 1}')
                id = input(f'Qual o id? ')
                salario_mes = input(f'Qual o salário mensal? ')
                bonus = input(f'Qual o bônus? ')
                if id.isdigit() and salario_mes.isdigit() and bonus.isdigit():
                    salarios.append([id, salario_mes, bonus])
                else:
                    print('Erro de instanciação!')
        else:
            print('Quantidade inválida')
    with open ('salarios.txt', 'w') as file:
        for i in range(len(salarios)):
            if i < (len(salarios) - 1):
                file.write(f'{salarios[i][0]};{salarios[i][1]};{salarios[i][2]}\n')
            else:
                file.write(f'{salarios[i][0]};{salarios[i][1]};{salarios[i][2]}')

def leitor_dados():
    '''Função que lê os arquivos e salva em matrizes'''
    try:
        with open ('funcionarios.txt', 'rt') as file:
            lista_aux = file.read().split('\n')
            for funcionario in range(len(lista_aux)):
                lista_funcionarios.append(lista_aux[funcionario].split(', '))
    except FileNotFoundError:
        print(f'Arquivo não encontrado! Criando funcionários.txt com valores predefinidos!')
        funcionarios = [['1', 'Maria', 'Gerente'], ['2', 'João', 'Analista'], ['3', 'Carlos', 'Desenvolvedor'], ['4', 'Ana', 'Designer']]
        with open ('funcionarios.txt', 'w', encoding = 'utf-8') as file:
            for i in range(len(funcionarios)):
                if i < (len(funcionarios) - 1):
                    file.write(f'{funcionarios[i][0]}, {funcionarios[i][1]}, {funcionarios[i][2]}\n')
                else:
                    file.write(f'{funcionarios[i][0]}, {funcionarios[i][1]}, {funcionarios[i][2]}')
        with open ('funcionarios.txt', 'rt') as file:
            lista_aux = file.read().split('\n')
            for funcionario in range(len(lista_aux)):
                lista_funcionarios.append(lista_aux[funcionario].split(', '))
    try:            
        with open ('salarios.txt', 'rt') as file:
            lista_aux = file.read().split()
            for salario in range(len(lista_aux)):
                lista_salarios.append(lista_aux[salario].split(';'))
    except FileNotFoundError:
        print(f'Arquivo não encontrado! Criando salários.txt com valores predefinidos!')
        salarios = [['1', '5000', '10000'], ['2', '4000', '5000'], ['3', '3000', '2000'], ['4', '2500', '3000']]
        with open ('salarios.txt', 'w') as file:
            for i in range(len(salarios)):
                if i < (len(salarios) - 1):
                    file.write(f'{salarios[i][0]};{salarios[i][1]};{salarios[i][2]}\n')
                else:
                    file.write(f'{salarios[i][0]};{salarios[i][1]};{salarios[i][2]}')
        with open ('salarios.txt', 'rt') as file:
            lista_aux = file.read().split()
            for salario in range(len(lista_aux)):
                lista_salarios.append(lista_aux[salario].split(';'))

def criar_relatório():
    '''Função que analisa e classifica o salário do funcionário'''
    for dados_funcionario in lista_funcionarios:
        for dados_salario in lista_salarios:
            if dados_funcionario[0] == dados_salario[0]:
                salario_mensal = float(dados_salario[1])
                bonus = float(dados_salario[2])
                salario_anual = (12*salario_mensal) + bonus
                if 40000 <= salario_anual <= 120000:
                    dados_funcionario.extend([salario_mensal, bonus, salario_anual, 'Dentro'])
                else:
                    dados_funcionario.extend([salario_mensal, bonus, salario_anual, 'Fora'])
        lista_funcionarios_atualizada.append(dados_funcionario)

def main():
    while True:
        print('\n1 - Criar arquivo dos funcionários\n2 - Criar arquivo de salários\n3 - Criar relatório')
        try:
            escolha = int(input('Qual função você deseja utilizar? '))
            if escolha == 1:
                criar_arquivo_funcionarios()
            elif escolha == 2:
                criar_arquivo_salarios()
            elif escolha == 3:
                leitor_dados()
                criar_relatório()
                with open ('relatorio_funcionarios.txt', 'wt', encoding = 'utf-8') as file:
                    for i in range(len(lista_funcionarios_atualizada)):
                        if '£' in lista_funcionarios_atualizada[i][1]: #isso não tem serventia alguma, só fiz porque o unicode tava me estressando
                            lista_funcionarios_atualizada[i][1] = str.replace(lista_funcionarios_atualizada[i][1].lower(),'£', '')
                            lista_funcionarios_atualizada[i][1] = lista_funcionarios_atualizada[i][1].replace(lista_funcionarios_atualizada[i][1][0], lista_funcionarios_atualizada[i][1][0].upper())
                        texto = ''
                        texto = f'ID: {lista_funcionarios_atualizada[i][0]}, Nome: {lista_funcionarios_atualizada[i][1]}, Cargo: {lista_funcionarios_atualizada[i][2]}, '
                        texto += f'Salário Mensal: {lista_funcionarios_atualizada[i][3]}, Bônus Anual: {lista_funcionarios_atualizada[i][4]}, '
                        texto += f'Salário Total Anual: {lista_funcionarios_atualizada[i][5]}, Faixa: {lista_funcionarios_atualizada[i][6]}\n'
                        if i < (len(lista_funcionarios_atualizada) - 1):
                            file.write(texto)
                        else:
                            file.write(texto[:-1])
                print('Sucesso! Confira seu arquivo "relatorios_funcionarios.txt"!')
                break
            else:
                print('Funcionalidade inválida!')
        except Exception as erro:
            print(f'{erro.__class__}')

if __name__ == '__main__':
    main()