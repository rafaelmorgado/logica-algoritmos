''' 23) Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário.
O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos.
Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados. '''

N = int(input("Entre com N: "))

if N > 1:
  divisores = 0
  for x in range(1, N):
    for divisor in range(1, x):
      if x % divisor == 0:
        divisores += 1
        if divisores > 1:
          break
    if divisores > 1:
      divisores = 0
      print(f"{x} não é primo")
    else:
      divisores = 0
      print(f"{x} é primo")