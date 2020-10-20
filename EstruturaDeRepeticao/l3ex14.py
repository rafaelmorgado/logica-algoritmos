''' 14) Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares e a quantidade de números impares. '''

contp = conti = 0

for x in range(1, 11):
  num = int(input("Entre com um número: "))
  if num % 2 == 0:
    contp = contp + 1
  else:
    conti = conti + 1

print("\nQuantidade de números pares: ", contp)
print("Quantidade de números ímpares: ", conti)