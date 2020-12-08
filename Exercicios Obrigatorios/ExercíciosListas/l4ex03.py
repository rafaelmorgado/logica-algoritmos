''' 3) Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores. '''

lista_numeros = []
PAR = []
IMPARES = []

soma_notas = 0
for x in range(1, 21):
  lista_numeros.append(int(input(f"Insira o {x}a número: ")))
  if lista_numeros[x-1] % 2 == 0:
    PAR.append(lista_numeros[x-1])
  else:
    IMPARES.append(lista_numeros[x-1])

print(f"\n Lista de Pares: {PAR}")
print(f"\n Lista de Ímpares: {IMPARES}")