''' 19) Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. '''

qt_num = int(input("Insira o tamanho do conjunto: "))

soma = 0

NUM_MENOR = 999
NUM_MAIOR = 0

while qt_num > 0:
  num = float(input("Entre com um número: "))
  while num > 0 and num < 1000:
    if num > NUM_MAIOR:
      NUM_MAIOR = num
      soma += NUM_MAIOR
      qt_num -= 1
      break
    if num < NUM_MENOR:
      NUM_MENOR = num
      soma += NUM_MENOR
      qt_num -= 1
      break
    soma += num
    qt_num -= 1
    break
  else:
    print("\nErro: Tente novamente! números entre(0-1000)")
else:
  print("\nFim do programa: tamanho do conjunto tem que ser maior que 0.")

print("\nMaior:",NUM_MAIOR)
print("Menor:",NUM_MENOR)
print("Soma dos números:",soma)