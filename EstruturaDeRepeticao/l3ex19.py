''' 19) Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. '''

qt_num = int(input("Entre com o tamanho do conjunto de números: "))
num = float(input("Entre com um número: "))

NUM_MENOR = NUM_MAIOR = soma_numeros = num

for x in range(1, qt_num):
  while num > 0 and num < 1000:
    num = float(input("Entre com um número: "))  
    if num > NUM_MAIOR:
      NUM_MAIOR = num
      soma_numeros += NUM_MAIOR
      break
    else: 
      comparador = num
      soma_numeros += num
      if comparador < NUM_MENOR:
        NUM_MENOR = num
        soma_numeros += num
        break
    break
  else:
    print("\nErro: Tente novamente! números entre(0-1000)")
    num = float(input("Entre com um número: "))

print("Maior:",NUM_MAIOR)
print("Menor:",NUM_MENOR)
print("Soma dos números:",soma_numeros)