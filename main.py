
#programa usando condicionais, para saber se o aluno foi suspenso ou 

tot_falta = int(input('informe o total de faltas: '))

if tot_falta == 1:
  print('pode entrar, porém caso tome mais duas faltas, irá ser suspenso.')

elif tot_falta == 2:
  print('tome cuidado, você só tem mais uma falta.')

else:
  print(f'você está suspenso. você ja tem {tot_falta} faltas.')