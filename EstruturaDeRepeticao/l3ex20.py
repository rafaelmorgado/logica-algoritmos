''' 20) Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. '''

fatorial = 1
num = int(input("Entre com um número: "))

while num > -1 and num < 16:
  for x in range(num, 1, -1):
    fatorial = fatorial*x
  print(f"{num:d}! = {fatorial:d}")
  fatorial = 1
  num = int(input("Entre com um número: "))
else:
  print("\nFim do programa:\nApenas fatorial de números inteiros positivos e menores que 16.")