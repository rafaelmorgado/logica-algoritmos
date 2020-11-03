''' 27) Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter mais de 40 alunos. '''

turmas = int(input("Informe a quantidade de turmas: "))
cont = total_alunos = 0

while turmas > 0:
  alunos_por_turma = int(input("Total de alunos por turma: "))
  while alunos_por_turma > 0:
    total_alunos += alunos_por_turma
    turmas -= 1
    cont += 1
    break

media_alunos_turma = total_alunos // cont
print("\nMédia de alunos por turma: %d" % media_alunos_turma)