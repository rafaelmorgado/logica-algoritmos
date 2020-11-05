''' 5) Faça um programa que leia 5 números e informe a soma e a média dos números. '''

soma = 0

for x in range(1, 6):
  num = float(input("Entre com os números: "))
  soma += num

media = soma/x
print("Soma: %.2f" % soma)
print("Média: %.2f " % media)