#Questão 3 - LabIdle 10 - Víctor BM
def busca (setor, infos):
    '''Retorna todos os funcionarios de determinado setor ao receber uma matriz
    cuja cada linha é: nome, registro, setor, telefone
    str, list -> list'''
    resposta = []
    for i in range(len(infos)):
        if setor in infos[i]:
            list.remove(infos[i], setor)
            list.append(resposta, infos[i])
    return resposta

def funcionarios():
    '''Função que cria uma matriz com as informações dos funcionarios
    none -> list'''
    quantidade = int(input('Qual a quantidade de funcionários na empresa? '))
    matriz = []
    for i in range(quantidade):
        linha = []
        print('O primeiro dado é o nome do funcionário, o segundo é o registro, o terceiro é seu setor e o quarto é seu telefone')
        for j in range(4):
            dado = str(input(f'Qual o dado {j + 1} do funcionario {i + 1}? '))
            list.append(linha, dado)
        list.append(matriz, linha)
    return matriz

def imprimidor (resposta):
    '''Função que imprime ao usuário sua busca e não retorna nada
    list -> none'''
    if len(resposta) == 0:
        print('Nenhum registro encontrado')
    else:
        for i in range(len(resposta)):
            print(resposta[i])

def main():
    infos = funcionarios()
    while True:
        setor = str(input('Qual setor você busca? '))
        imprimidor(busca(setor, infos)) 
        repetidor = str(input('Você deseja usar a função novamente? [S ou N] ')).lower()
        if repetidor == 'n':
            break
main()
