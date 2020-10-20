''' 7) Faça um programa que leia 5 números e informe o maior número. '''

num = float(input("Entre com um número: "))
NUM_MAIOR = num

for x in range(1, 5):
  num = float(input("Entre com um número: "))
  if num > NUM_MAIOR:
    NUM_MAIOR = num

print("Maior:",NUM_MAIOR)