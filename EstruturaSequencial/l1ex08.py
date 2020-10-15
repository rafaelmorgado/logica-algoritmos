''' 8) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês. '''

valor_hora = float(input("Entre com valor ganho por hora: "))
hora_trabalhada = float(input("Entre com nmro/horas trabalhada: "))

total_salario = valor_hora * hora_trabalhada
print("Total salário ganho no mês: %.2f" % total_salario)