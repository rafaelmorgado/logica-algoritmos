''' 7) Faça um programa que receba dois números inteiros (início e fím)e imprima os números inteiros compreendidos no intervalo (o número inicial e final devem ser impressos também). '''

print("Digite o número inicial")
inicio = int(input())
print("Digite o número final")
fim = int(input())

if inicio < fim:
  for x in range(inicio, fim+1):
    print(x)
if inicio > fim:
  for x in range(inicio, fim-1, -1):
    print(x)
if inicio == fim:
  print("Erro: números iguais")