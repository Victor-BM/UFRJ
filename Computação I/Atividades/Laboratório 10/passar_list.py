def main():
  while True:
    a = list(eval(input('Dê uma lidta: ')))
    print (a)
#se usuário passar: 'banana',
#então fica ['banana']
#eval transforma em tupla quando separado por vírgulas
#se usuário passar: 'banana'
#entao fica: ['b', 'a', 'n', 'a', 'n', 'a']
main()
