''' 11) As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
-> salários até R$ 280,00 (incluindo) : aumento de 20%
-> salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
-> salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
-> salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
-> o salário antes do reajuste;
-> o percentual de aumento aplicado;
-> o valor do aumento;
-> o novo salário, após o aumento. '''

salario = float(input("Informe o salário R$: "))

if salario > 0 and salario <= 280:
  percentual_aumento = .20
  valor_aumento = salario * percentual_aumento
  novo_salario = valor_aumento + salario
elif salario > 280 and salario <= 700:
  percentual_aumento = .15
  valor_aumento = salario * percentual_aumento
  novo_salario = valor_aumento + salario
elif salario > 700 and salario <= 1500:
  percentual_aumento = .10
  valor_aumento = salario * percentual_aumento
  novo_salario = valor_aumento + salario
elif salario > 1500:
  percentual_aumento = .05
  valor_aumento = salario * percentual_aumento
  novo_salario = valor_aumento + salario

print(f"\nSalário antes do reajuste R$: {salario:.2f}")
print(f"Percentual aumento: {percentual_aumento*100:.0f}%")
print(f"Valor do aumento R$: {valor_aumento:.2f}")
print(f"Novo salário R$: {novo_salario:.2f}")