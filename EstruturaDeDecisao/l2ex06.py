''' 6) Faça um Programa que leia três números e mostre o maior deles. '''

n1 = float(input("Entra com o 1a número: "))
n2 = float(input("Entra com o 2a número: "))
n3 = float(input("Entra com o 3a número: "))

if n1 > n2 and n1 > n3:
  print(n1, "é o maior")
elif n2 > n1 and n2 > n3:
  print(n2, "é o maior")
elif n3 > n1 and n3 > n2:
  print(n3, "é o maior")
else:
  print("Os números são iguais")