''' 28) Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor para em cada um. '''

total_investido = cont  = 0

cds = int(input("Informe a quantidade de CDs: "))

while cds > 0:
  valor_cd = float(input("Informe o valor dos CDs: R$ "))
  while valor_cd > 0:
    total_investido += valor_cd
    cds -= 1
    cont += 1
    break

media_alunos_turma = total_investido // cont
print("\nTotal investido: %.2f" % total_investido)
print("Média de gastos por CDs: R$ %.2f" % media_alunos_turma)