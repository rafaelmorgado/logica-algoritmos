''' 22) Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível. '''

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
    for x in range(1, numero + 1):
      if numero % x == 0:
        divisor += divisor
        print(f"{numero} é divisível por {x}")
  else:
    print(f"{numero} não é primo")