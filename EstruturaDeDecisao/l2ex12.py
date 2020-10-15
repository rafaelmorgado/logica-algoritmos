''' 12) Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
        Salário Bruto: (5 * 220)        : R$ 1100,00
        (-) IR (5%)                     : R$   55,00  
        (-) INSS ( 10%)                 : R$  110,00
        FGTS (11%)                      : R$  121,00
        Total de descontos              : R$  165,00
        Salário Liquido                 : R$  935,00 '''

valor_hora = float(input("Informe o valor hr/trabalhada: "))
horas_trabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salario_bruto = valor_hora * horas_trabalhadas
sindicato = salario_bruto * .03
FGTS = salario_bruto * .11
INSS = salario_bruto * .10

if salario_bruto > 0 and salario_bruto <= 900:
  print("Isento")
elif salario_bruto > 900 and salario_bruto <= 1500:
  percentual_IR = .05
  IR = salario_bruto * percentual_IR
  descontos = sindicato + IR + INSS
  salario_liquido = salario_bruto - descontos
elif salario_bruto > 1500 and salario_bruto <= 2500:
  percentual_IR = .10
  IR = salario_bruto * percentual_IR
  descontos = sindicato + IR + INSS
  salario_liquido = salario_bruto - descontos
elif salario_bruto > 2500:
  percentual_IR = .20
  IR = salario_bruto * percentual_IR
  descontos = sindicato + IR + INSS
  salario_liquido = salario_bruto - descontos
else:
  print("\nDados inválidos:\nOs valores necessitam ser maiores que zero.")

print(f"\nSalário Bruto: ({valor_hora:.2f} * {horas_trabalhadas:.2f})  : R$ {salario_bruto:.2f}")
print(f"(-) IR ({percentual_IR*100:.0f}%): R$ {IR:.2f}")
print(f"(-) INSS (10%): R$ {INSS:.2f} ")
print(f"FGTS (11%): R$ {FGTS:.2f} ")
print(f"Total de descontos: R$ {descontos:.2f} ")
print(f"Salário Liquido: R$ {salario_liquido:.2f} ")