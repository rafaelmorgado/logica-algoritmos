''' 21) Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. '''

num = int(input("Entre com um número: "))

if num == 1:
  print("não é primo:", num)

if num > 1:
  eprimo = True
  divisor = 2
  while divisor <= num and eprimo:
    if num % divisor == 0:
      if num == 2:
        eprimo = True
      else:
        eprimo = False
        print("não é primo:",num)
    if eprimo:
      print("é primo:",num)
      break