''' 23) Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes (divisões) executados. '''

N = int(input("Entre com N: "))

cont = 0

for x in range(0, N):
  if x >= 0:
    eprimo = 1
    divisor = 2
    while divisor <= x-1 and eprimo:
      if x % divisor == 0:
        eprimo = 0
        divisor += divisor
        cont += 1
        print("não é primo:",x)
      if eprimo:
        print("é primo:",x)
        break