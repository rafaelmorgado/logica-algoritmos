''' 39) Faça um programa que leia dez conjuntos de dois valores, o primeiro representando o número do aluno e o segundo representando a sua altura em centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas. '''

print("\nAluno:")
numero_aluno = int(input("Número do aluno: "))
altura = int(input("Altura em cm: "))

altura_maior = altura_menor = altura
aluno_maior_altura = aluno_menor_altura = numero_aluno

while altura != 0 and numero_aluno != 0:
  if altura > altura_maior:
    altura_maior = altura
    aluno_maior_altura = numero_aluno
  if altura < altura_menor:
    altura_menor = altura
    aluno_menor_altura = numero_aluno
  if altura == 0 and numero_aluno == 0:
    break
  print("\nAluno:")
  numero_aluno = int(input("Número do aluno: "))
  altura = int(input("Altura: "))

print(f"\nAluno(a): número {aluno_maior_altura} é o mais alto com: {altura_maior} cm")
print(f"Aluno(a): número {aluno_menor_altura} é o mais baixo com: {altura_menor} cm")