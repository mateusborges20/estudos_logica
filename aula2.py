
#programa que encontra o maior entre dois números
#utilizando condicionais

primeiro_valor = input('digite o primeiro valor:')
segundo_valor = input('digite o segundo valor:')


if int(primeiro_valor) > int(segundo_valor):
  print('o primeiro valor é maior')

elif int(primeiro_valor) < int(segundo_valor):
  print('o segundo valor é maior')

else:
  print('os valores são iguais')

