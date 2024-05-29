# Programa que gera um valor aleatorio de 1 a 10 e permite que o usuario chute um numero
# até que o valor aleatorio gerado no inicio do programa seja chutado corretamente.

import random

valor_aleatorio = random.randint(1,10)

acertou = False

while acertou == False:
  chute = int(input('Chute um numero de 1 a 10: '))
  if chute > valor_aleatorio:
    print(f'o valor aleatorio foi {valor_aleatorio} e voce chutou o valor {chute}')
    print('Chute foi maior que o valor gerado')
  
  elif chute < valor_aleatorio:
    print(f'o valor aleatorio foi {valor_aleatorio} e voce chutou o valor {chute}')
    print('chute foi menor que o valor gerado')
    
  elif chute == valor_aleatorio:
    acertou = True
    print('chute foi igual ao valor gerado')
    print('Parabéns, você acertou!')
  