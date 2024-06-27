#Trabalho Final - ContatinhosApp - Parte 2 - Víctor BM
import contatinhosbib as cbib
contatos = []






def teste():
    contatos = [['João Fields', ['11', '13'], 'aa', 'insta'], ['Ana Fieldson', '23', '', '']]
    cbib.contatos_geral = contatos
    ind = 0
    print(cbib.buscar_contato(contatos, 'Fields'))
    cbib.atualizar_contato(contatos[ind], 1, '12')
    print(contatos)
    cbib.excluir_telefone(contatos[ind],'12')
    contatos = cbib.contatos_geral
    print(contatos)
    print(cbib.quem_ligou('37'))
    cbib.criar_contato('Joana', '32323')
    print(contatos)
teste()
