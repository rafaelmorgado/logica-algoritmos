''' 1) Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa. '''

vetor_numeros = []

for x in range(1, 11):
  vetor_numeros.append(float(input(f"Insira a {x} nota: ")))

print(f"Lista antes: {vetor_numeros}")
vetor_numeros.reverse()
print(f"Lista inversa: {vetor_numeros}")