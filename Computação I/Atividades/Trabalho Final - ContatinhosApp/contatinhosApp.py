#Trabalho Final - ContatinhosApp - Parte 2 - Víctor BM
import contatinhosbib as cbib
contatos = []







def teste():
    contatos = [['João Fields', '11', 'aa', 'insta'], ['Ana Fieldson', '12', '', '']]
    ind = 0
    print(cbib.buscar_contato(contatos, 'Fields'))
    list.insert(contatos, ind, cbib.atualizar_contato(contatos[ind], 1, '12'))
    list.remove(contatos, contatos[ind+1])
    print(contatos)
    list.insert(contatos, ind, cbib.excluir_telefone(contatos[ind],'12'))
    list.remove(contatos, contatos[ind+1])
    print(contatos)
    print(cbib.quem_ligou(contatos, '12'))
teste()