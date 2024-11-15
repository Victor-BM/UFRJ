ignorar = ['.', ',', '!', ':', ':', '?', '/', '-', '"', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
palavras = {}
três_ocorrências = {}

def leitor_redacao(arquivo):
    '''Função que cria que trata o texto do arquivo e cria um dicionário com suas palavras'''
    texto_base = ''
    try:
        with open(arquivo, 'rt', encoding = 'utf-8') as file:
            lista_redação = file.read().split('\n')
    except Exception as erro:
        print(f'{erro.__class__}')
        return False
    else:
        for linha in lista_redação:
            linha = linha.lower()
            for element in ignorar:
                linha = linha.replace(element, '')
            for palavra in linha.split():
                if len(palavra) > 1: 
                    texto_base += palavra + ' '
                    if palavra not in palavras:
                        palavras[palavra] = 0
        return texto_base

def contador_palavras(texto_tratado):
    '''Função que conta a quantidade de repetições'''
    quantidades = []
    for palavra in palavras.keys():
        palavras[palavra] = texto_tratado.split().count(palavra)
    for valor in palavras.values():
        quantidades.append(valor)
    quantidades.sort()
    quantidades = quantidades[::-1]
    return (quantidades)

def classificador_ocorrencias(quantidades):
    '''Função que classifica as 3 palavras que mais ocorreram no texto'''
    for i in range(0, 3):
        for palavra in palavras.keys():
            if palavras[palavra] == quantidades[i]:
                três_ocorrências[palavra] = quantidades[i]
            if len(três_ocorrências.keys()) == 3:
                break

def main():
    try:
        arquivo = input('Digite o nome do arquivo a ser analisado (Ex: redação.txt): ')
        texto_tratado = leitor_redacao(arquivo)
        if texto_tratado:
            quantidades = contador_palavras(texto_tratado)
            classificador_ocorrencias(quantidades)
            with open('três_ocorrências.txt', 'w', encoding = 'utf-8') as file:
                lista_palavras = []
                for palavra in três_ocorrências.keys():
                    lista_palavras.append(palavra)
                for i in range(len(lista_palavras)):
                    if i < ((len(lista_palavras)) - 1):
                        file.write(f'{lista_palavras[i]}: {três_ocorrências[lista_palavras[i]]}\n')
                    else:
                        file.write(f'{lista_palavras[i]}: {três_ocorrências[lista_palavras[i]]}')
            print('Sucesso! Confira seu arquivo "três_ocorrências.txt"!')
    except Exception as erro:
        print(f'{erro.__class__}')

if __name__ == '__main__':
    main()