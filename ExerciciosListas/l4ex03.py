''' 3) Faça um Programa que leia 4 notas, mostre as notas e a média na tela. '''

lista_notas = []
soma_notas = 0
for x in range(1, 5):
  lista_notas.append(float(input(f"Insira a {x} nota: ")))
  soma_notas += lista_notas[x-1]

media = soma_notas / x
print(f"Notas: {lista_notas}")
print(f"Média das notas: {media}")