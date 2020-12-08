''' 4) Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes. '''

lista_consoantes = []
total_consoantes = 0

for x in range(10):
  letra = str(input("Insira uma letra: ").upper())
  if letra != 'A' and letra != 'E' and letra != 'I' and letra != 'O' and letra != 'U':
    lista_consoantes.append(letra)
    total_consoantes += 1
  else:
    x -= 1

print(f"\nListas de consoantes: {lista_consoantes} = {total_consoantes} consoantes")