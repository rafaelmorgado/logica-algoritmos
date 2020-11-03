''' 32) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120 '''

fatorial = 1
num = abs(int(input("Entre com um número: ")))

if num >= 1:
  print(f"\nFatorial de: {num:d}")
  print(f"{num:d}! =",end=" ")
  for x in range(num, 1, -1):
    fatorial = fatorial*x
    print(f"{x} .",end=" ")
  print(f"1 = {fatorial:d}")
else:
  print(f"{num:d}! = {fatorial:d}")