#Teste 3 - Víctor BM

#Q1
def emails_update(contatos):
    '''Atualiza o e-mail para que possa adicionar novos e-mails
    list -> nome'''
    i = 0
    while i < len(contatos):
        email = contatos[i][2]
        contatos[i][2] = [email]
        i += 1

#Q2
def contaestrelas (aval):
    '''Função que retorna quantas estrelas
    de cada tipo o motorista ganhou
    list -> list'''
    total_estrelas= [0, 0, 0, 0, 0]
    i = 0
    while i<len(aval):
        j = 1
        while j<=5:
            count = 0
            if aval[i] == j:
                count = total_estrelas[j-1]
                count += 1
                total_estrelas[j-1] = count
                break
            j +=1
        i += 1
    return total_estrelas
    
#Q3
def contaestrelas_v2 (aval):
    '''Função que retorna quantas estrelas
    de cada tipo o motorista ganhou
    list -> list'''
    total_estrelas= {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}
    i = 0
    while i<len(aval):
        j = 1
        while j<=5:
            count = 0
            if aval[i] == j:
                count = total_estrelas[j]
                count += 1
                total_estrelas[j] = count
                break
            j +=1
        i += 1
    return total_estrelas
    
