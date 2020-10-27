''' 22) Altere o programa de cálculo dos números primos, informando, caso o número não seja primo, por quais número ele é divisível. '''

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
        print(f"não é primo: {num}")
        for x in range(1, num+1):
          if num % x == 0:
            divisor += divisor
            print(f"é divisível por {x}")
      if eprimo:
        print("é primo:",num)
        break