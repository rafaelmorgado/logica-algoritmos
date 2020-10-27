''' 22) Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível. '''

num = int(input("Entre com um número: "))

if num >= 0:
  eprimo = 1
  divisor = 2
  while divisor <= num-1 and eprimo:
    while num % divisor == 0:
      eprimo = 0
      divisor += divisor
      print(f"não é primo: {num}, e é divisível por: {divisor}")
    if eprimo:
      print("é primo:",num)
      break