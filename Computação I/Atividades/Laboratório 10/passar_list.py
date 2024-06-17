def main():
  while True:
    a = list(eval(input('Para passar uma lista, dê cada entrada atribuída ao indíce separadas por vírgulas: ')))
    print (a)
#se usuário passar: 'banana',
#então fica ['banana']
#eval transforma em tupla quando separado por vírgulas
#se usuário passar: 'banana'
#entao fica: ['b', 'a', 'n', 'a', 'n', 'a']
main()
