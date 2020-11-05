''' 1) Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido. '''

nota = float(input("Entre com uma nota: "))

while True: 
  if nota >= 0 and nota <= 10:
    print("Nota válida: %.2f" % nota)
    nota = int(input("\nEntre com um nota: "))
  else:
    print("Nota inválida: %.2f" % nota)
    nota = int(input("\nEntre com um nota: "))