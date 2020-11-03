''' 35) Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma lista dos números primos existentes entre 1 e um número inteiro informado pelo usuário. '''

N = int(input("Entre com N: "))

if N > 1:
  divisores = 0
  for numero in range(1, N):
    for divisor in range(1, numero):
      if numero % divisor == 0:
        divisores += 1
        if divisores > 1:
          break
    if divisores > 1:
      divisores = 0
      print(f"{numero} não é primo")
    else:
      divisores = 0
      print(f"{numero} é primo")