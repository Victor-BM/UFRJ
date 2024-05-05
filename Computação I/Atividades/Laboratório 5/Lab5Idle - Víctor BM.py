#Lab5Idle - Víctor BM
#Q1
#A
def criar_contato (nome, telefone = '', email = '', instagram = ''):
    '''Função que permite criar contatos com apenas o nome obrigatório
    str, str, str, str -> list'''
    telefones = [telefone,]
    contato = [nome, telefones, email, instagram]
    return contato

#B
def atualizar_contato (contato, indice, nova_inf):
    '''Função que permite atualizar o contato adicionando uma nova informação pelo indice
    0 -> nome; 1 -> telefones; 2 -> email, 3 -> instagram
    list, str, int, str -> bool'''
    if indice == 0 or indice == 2 or indice == 3:
        contato[indice] = nova_inf
        return True
    elif indice == 1 and (nova_inf != contato[1][0]):
        contato[1][1:] = nova_inf
        return True
    else:
        return False

#Q2
def traducao_rnaM (rna):
    '''Função que recebe uma molécula de rna mensageiro (3 trincas de rna) e
    retorna uma cadeia de 3 aminoácidos
    str -> list'''
    aminoacido = {'UUU' : 'Phe', 'CUU' : 'Leu', 'UUA' : 'Leu', 'AAG' : 'Lisina',
                  'UCU' : 'Ser', 'UAU' : 'Tyr', 'CAA' : 'Gln'}
    a = aminoacido[rna[0:3]]
    b = aminoacido[rna[3:6]]
    c = aminoacido[rna[6:]]
    cadeia = [a, b, c]
    return cadeia
    
    
