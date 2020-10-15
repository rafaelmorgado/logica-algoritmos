''' 22) Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão). '''

num = int(input("Entre com um número: "))

if num % 2 == 0:
  print(num, "é par")
else:
  print(num, "é ímpar")