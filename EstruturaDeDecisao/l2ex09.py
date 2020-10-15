''' 9) Faça um Programa que leia três números e mostre-os em ordem decrescente. '''

n1 = float(input("Entre com o 1a número: "))
n2 = float(input("Entre com o 2a número: "))
n3 = float(input("Entre com o 3a número: "))

if n1 < n2:
  aux = n1
  n1 = n2
  n2 = aux
if n1 < n2:
  aux = n1
  n1 = n2
  n2 = aux
if n2 < n3:
  aux = n1
  n1 = n2
  n2 = aux

print("Ordem Decrescente:", n1, n2, n3)