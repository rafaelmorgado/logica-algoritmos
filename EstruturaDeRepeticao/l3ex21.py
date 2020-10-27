''' 21) Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. '''

num = int(input("Entre com um número: "))

if num >= 0:
  eprimo = 1
  divisor = 2
  while divisor <= num-1 and eprimo:
    if num % divisor == 0:
      eprimo = 0
      divisor += divisor
      print("não é primo:",num)
    if eprimo:
      print("é primo:",num)
      break