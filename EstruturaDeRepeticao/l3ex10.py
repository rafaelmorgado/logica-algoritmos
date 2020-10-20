''' 10) Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. '''

num1 = int (input("Entre com um número: "))
num2 = int (input("Entre com um número: "))

if num1 > num2:
  for x in range(num2, num1-1):
    print(x+1)
if num1 < num2:
  for x in range(num1, num2-1):
    print(x+1)
if num1 == num2:
  print("Erro: números iguais")