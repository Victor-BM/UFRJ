#LabIDLE 6 - Víctor BM

#Q1
#a
def excluir_contato (contato, telefone):
    '''Função que permite excluir o telefone do contato
    list, string -> bool'''
    if telefone in contato:
        list.remove(contato, telefone)
        return True
    else:
        return False

#Q2
def campeonato(tabela):
    '''Função que recebe uma tabela de times com seus pontos e fornece
    ua lista de times, os pontos do campeão e a média de pontos
    dict -> list'''
    infos = []
    list.insert(infos, 0, list(dict.keys(tabela)))
    a = list(dict.values(tabela))
    campeao = max(a)
    list.append(infos, campeao)
    media = (sum(a))/(len(a))
    list.append(infos, media)
    return infos
    
    
        
