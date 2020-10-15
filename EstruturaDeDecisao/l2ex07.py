''' 7) Faça um Programa que leia três números e mostre o maior e o menor deles. '''

n1 = float(input("Entre com o 1a número: "))
n2 = float(input("Entre com o 2a número: "))
n3 = float(input("Entre com o 3a número: "))
maior = menor = 0
if n1 > n2 and n1 > n3:
  maior = n1
  if n2 > n3:
    menor = n3
  else:
    menor = n2
elif n2 > n1 and n2 > n3:
  maior = n2
  if n1 > n3:
    menor = n3
  else:
    menor = n1
elif n3 > n1 and n3 > n2:
  maior = n3
  if n1 > n2:
    menor = n2
  else:
    menor = n1
else:
  print('números iguais')

print(maior, "é o maior")
print(menor, "é o menor")