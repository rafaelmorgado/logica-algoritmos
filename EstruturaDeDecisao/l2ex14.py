''' 14) Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à tabela abaixo: 
Média de Aproveitamento  Conceito
Entre 9.0 e 10.0        A
Entre 7.5 e 9.0         B
Entre 6.0 e 7.5         C
Entre 4.0 e 6.0         D
Entre 4.0 e zero        E '''

n1 = float(input("Insira n1: "))
n2 = float(input("Insira n2: "))

media = (n1 + n2) / 2

if media > 9 and media <= 10:
  print(f"\nNota1: {n1:.2f}\nNota2: {n2:.2f}\nMédia: {media:.2f}")
  print("Conceito: A - APROVADO")
elif media > 7.5 and media <= 9:
  print(f"\nNota1: {n1:.2f}\nNota2: {n2:.2f}\nMédia: {media:.2f}")
  print("Conceito: B - APROVADO")
elif media > 6 and media <= 7.5:
  print(f"\nNota1: {n1:.2f}\nNota2: {n2:.2f}\nMédia: {media:.2f}")
  print("Conceito: C - APROVADO")
elif media > 4 and media <= 6:
  print(f"\nNota1: {n1:.2f}\nNota2: {n2:.2f}\nMédia: {media:.2f}")
  print("Conceito: D - REPROVADO")
elif media >= 0 and media < 4:
  print(f"\nNota1: {n1:.2f}\nNota2: {n2:.2f}\nMédia: {media:.2f}")
  print("Conceito: E - REPROVADO")
else:
  print("Favor inserir valores positivos")