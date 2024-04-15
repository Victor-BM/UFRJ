#Lab3MT - Víctor BM

#Q1
def classifica (C, Ce, Cs, Fv, Fe, Fs):
    '''Função que define qual é o time melhor classificado ou se há empate
    int, int, int, int, int, int -> string'''
    ponto_c = C*3 + Ce
    ponto_f = Fv*3 + Fe
    if ponto_c == ponto_f:
        if Cs == Fs:
            return 'Empate'
        elif Cs > Fs:
            return 'Cormengo'
        else:
            return 'Flaminthias'
    elif ponto_c > ponto_f:
        return 'Cormengo'
    else:
        return 'Flaminthias'

#Q2
def avioes (competidores, quantidade_papel, quantidade_folha):
    '''Função que retorna se a quantidade de folhas comprada pela diretora é suficiente
    int, int, int -> string'''
    if (competidores*quantidade_folha) <= quantidade_papel:
        return 'Suficiente'
    else:
        return 'Insuficiente'
        
