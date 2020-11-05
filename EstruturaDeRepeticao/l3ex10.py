''' 10) Faça um programa que receba dois números inteiros e gere os números inteiros que estão no intervalo compreendido por eles. '''

inicio = int(input("Entre com o 1a número: "))
fim = int(input("Entre com o 2a número: "))

if inicio < fim:
  for x in range(inicio, fim+1):
    print(x)
if inicio > fim:
  for x in range(inicio, fim-1, -1):
    print(x)
if inicio == fim:
  print("Erro: números iguais")