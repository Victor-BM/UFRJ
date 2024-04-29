#Lab4Idle - Víctor BM

#Q1
def SIGA (info_aluno):
    '''Função que calcula a média de um aluno e sua situação
    tupla (nome, nota 1, nota 2, nota 3) -> tupla (nome, média, situação)'''
    media = (info_aluno[1] + info_aluno[2] + info_aluno[3])/3
    media = round (media, 1)
    if media >= 7:
        return (info_aluno[0], media, 'Parabéns!')
    elif media >= 5:
        return (info_aluno[0], media, 'aprovado')
    else:
        (info_aluno[0], media, 'reprovado')

#Q2
def zodiaco (ano):
    '''Função que recebe o ano de nascimento e retorna o seu signo no zodíaco chinês
    int -> str'''
    signo = ('Macaco', 'Galo', 'Cão', 'Porco', 'Rato', 'Boi',
             'Tigre', 'Coelho', 'Dragão', 'Serpente', 'Cavalo', 'Carneiro')
    indice = ano%12
    return signo[indice]   

#Q3
def telefone (numero):
    '''Função que verifica se um número de telefone é válido e retorna uma tupla
    informando o DDD e o número sem o DDD
    str -> tuple'''
    tamanho = len(numero)
    if tamanho == 8 or tamanho == 9:
        return ('', numero)
    elif tamanho == 10:
        return (numero[0:2], numero[2:10])
    elif tamanho == 11:
        return (numero[0:2], numero[2:11])
    else:
        return ('','')


#Q4
def formato_data (data):
    '''Função que recebe uma data no formato xx/xx/xx e interpreta se é:
    dd/mm/yy, mm/dd/yy, yy/mm/dd ou inválida
    string -> tuple'''
    dig0_1 = int(data[0:2])
    dig3_4 = int(data[3:5])
    dig6_7 = int(data[6:8])
    possiveis_formatos = ()
    if (dig0_1 >= 1 and dig0_1 <= 31) and (dig3_4 >= 1 and dig3_4 <= 12) and (dig6_7 >= 0):
        possiveis_formatos = possiveis_formatos + ('dd/mm/yy',)
    if(dig0_1 >= 1 and dig0_1 <= 12) and (dig3_4 >= 1 and dig3_4 <= 12) and (dig6_7 >= 0):
        possiveis_formatos = possiveis_formatos + ('mm/dd/yy',)
    if(dig0_1 <= 12) and (dig3_4 >= 1 and dig3_4 <= 12) and (dig6_7 >= 1 and dig6_7 <= 12):
        possiveis_formatos = possiveis_formatos + ('yy/mm/dd',)
    return possiveis_formatos
