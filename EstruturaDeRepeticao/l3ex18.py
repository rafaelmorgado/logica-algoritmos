''' 18) Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores. '''

qt_num = int(input("Insira o tamanho do conjunto: "))

num = float(input("Entre com um número: "))
NUM_MAIOR = NUM_MENOR = num
soma = 0

while qt_num > 0:
  if num > NUM_MAIOR:
    NUM_MAIOR = num
  if num < NUM_MENOR:
    NUM_MENOR = num
  soma += num
  qt_num -= 1
  if qt_num == 0:
    break
  num = float(input("Entre com um número: "))

print("\nMaior:",NUM_MAIOR)
print("Menor:",NUM_MENOR)
print("Soma dos números:",soma)