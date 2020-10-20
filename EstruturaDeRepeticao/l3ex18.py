''' 18) Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores. '''

qt_num = int(input("Entre com o tamanho do conjunto de números: "))
num = float(input("Entre com um número: "))
NUM_MENOR = soma_numeros = NUM_MAIOR = num

for x in range(1, qt_num):
  num = float(input("Entre com um número: "))
  if num > NUM_MAIOR:
    NUM_MAIOR = num
    soma_numeros += NUM_MAIOR
  else: 
    comparador = num
    soma_numeros += num
    if comparador < NUM_MENOR:
      NUM_MENOR = num
      soma_numeros += num

print("Maior:",NUM_MAIOR)
print("Menor:",NUM_MENOR)
print("Soma dos números:",soma_numeros)