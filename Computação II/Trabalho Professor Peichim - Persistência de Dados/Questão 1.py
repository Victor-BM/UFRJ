lista_empregados = []
lista_departamentos = []
lista_empregados_atualizada = []

def leitor_dados():
    '''Função que lê os arquivos e salva em matrizes'''
    try:
        with open ('empregados.txt', 'rt') as file:
            lista_aux = file.read().split('\n')
            for empregado in range(len(lista_aux)):
                lista_empregados.append(lista_aux[empregado].split(','))
        with open ('departamentos.txt', 'rt') as file:
            lista_aux = file.read().split()
            for departamento in range(len(lista_aux)):
                lista_departamentos.append(lista_aux[departamento].split(','))
        return True
    except FileNotFoundError:
        print(f'Arquivo não encontrado')
        return False

def analise_departamento():
    '''Função que analisa se os empregado estão em um departamento'''
    for dados_empregado in lista_empregados:
        dados_empregado.append('Departamento ausente')
        for dados_departamento in lista_departamentos:
            if dados_empregado[0] == dados_departamento[0]:
                dados_empregado[3] = dados_departamento[1]
        lista_empregados_atualizada.append(dados_empregado)

def main():
    if leitor_dados():
        analise_departamento()
        with open ('empregadosComDepartamentos.txt', 'w') as file:
            for i in range(len(lista_empregados_atualizada)):
                if i < (len(lista_empregados_atualizada) - 1):
                    file.write(f'{lista_empregados_atualizada[i][0]}, {lista_empregados_atualizada[i][1]}, {lista_empregados_atualizada[i][2]}, {lista_empregados_atualizada[i][3]}\n')
                else:
                   file.write(f'{lista_empregados_atualizada[i][0]}, {lista_empregados_atualizada[i][1]}, {lista_empregados_atualizada[i][2]}, {lista_empregados_atualizada[i][3]}') 
        print('Sucesso! Confira seu arquivo "empregadosComDepartamentos.txt"!')

if __name__ == '__main__':
    main()