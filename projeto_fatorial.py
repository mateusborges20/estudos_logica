
#exemplo utilizando tratamento de erros, laços e condicionais
while True:
  try:
    numero = int(input('informe um numero:'))
    if numero < 0:
      print('informe um numero positivo')

    if numero > 0:
      fat = 1
      for valor in range(fat, numero+1):
        fat*=valor
      print('O Fatorial de {} é {}'.format(numero, fat))
      break
    
  except ValueError:
    print('informe um numero inteiro:')





#exemplo utilizando laços e condições
fat = 1

numero = 0

while numero <= 0:
  numero = int(input('informe um numero:'))
  if numero <= 0:
    print('informe um numero positivo')
  else:
    if numero > 0:
      for valor in range(fat, numero+1):
        fat*=valor
      print('O Fatorial de {} é {}'.format(numero, fat))
  print('fim do programa')