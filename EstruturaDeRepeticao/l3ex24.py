''' 24) Faça um programa que calcule o mostre a média aritmética de N notas.'''

cont = notas = 0

N = int(input("Entre com o número de notas: "))

for x in range(N):
  nota = float(input("Entre com uma nota: "))
  while 0 <= nota <= 10:
    notas += nota
    cont += 1
    break
  else:
    print("\nErro: Tente novamente! notas entre(0-10)")

media_aritmetica = notas / cont
print("Média Aritmética: %.2f" % media_aritmetica)