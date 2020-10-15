''' 8) Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato. '''

p1 = float(input("Insira o preço do 1a produto R$: "))
p2 = float(input("Insira o preço do 2a produto R$: "))
p3 = float(input("Insira o preço do 3a produto R$: "))

if p1 < p2 and p1 < p3:
  print("1a produto é o mais barato: R$", p1)
elif p2 < p1 and p2 < p3:
  print("2a produto é o mais barato: R$", p2)
elif p3 < p1 and p3 < p2:
  print("3a produto é o mais barato: R$", p3)
else:
  print("Os preços são iguais")