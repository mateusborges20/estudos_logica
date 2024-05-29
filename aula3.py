from time import sleep

#laços de repetição e listas em python.

#imprima valores de 1 a N

valor_minimo = int(input('qual o valor mínimo? '))
valor_maximo = int(input('qual o valor máximo? '))

for numero in range(valor_minimo, valor_maximo + 1):
  sleep(0.4)
  print(numero)
  
print('fim da contagem!')




#listas em python (some  os valores de uma lista)

idades = [15, 46, 75, 34, 23]

# utlizando o for loop para iterar sobre a lista

soma_idades = 0

for idade in idades:
  soma_idades += idade
print(f'A soma de todas  as idades é {soma_idades}')