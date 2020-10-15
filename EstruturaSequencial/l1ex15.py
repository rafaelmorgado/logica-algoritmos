''' 15) Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela abaixo:
+ Salário Bruto : R$
- IR (11%) : R$
- INSS (8%) : R$
- Sindicato ( 5%) : R$
= Salário Liquido : R$ '''

valor_hora = float(input("Entre com valor ganho por hora:" ))
hora_trabalhada = float(input("Entre com nmro/horas trabalhadas: "))

salario_bruto = valor_hora * hora_trabalhada
print("salario bruto : R$ %.2f" % salario_bruto)

IR = salario_bruto * .11
INSS = salario_bruto * .08
SINDICATO = salario_bruto * .05 

salario_liquido = salario_bruto - IR - INSS - SINDICATO

print("IR (11%) : R$", IR)
print("INSS (8%) : R$", INSS)
print("Sindicato (5%) : R$", SINDICATO)
print("salario líquido : R$", salario_liquido)