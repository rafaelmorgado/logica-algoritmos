''' 21) Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. Um número primo é aquele que é divisível somente por ele mesmo e por 1. '''

numero = int(input("Entre com um número: "))

if numero == 0 or numero == 1:
  print("não é primo:", numero)

if numero > 1:
  divisores = 0
  for divisor in range(1, numero):
    if numero % divisor == 0:
      divisores += 1
      if divisores > 1:
        break
  if divisores > 1:
    print(f"{numero} não é primo")
  else:
    print(f"{numero} é primo")