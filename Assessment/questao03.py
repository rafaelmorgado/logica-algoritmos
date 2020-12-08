c_VALOR_MAX_MORADIA = .3
porcentagem_moradia = int(c_VALOR_MAX_MORADIA * 100)
c_VALOR_MAX_EDUCACAO = .2
porcentagem_educacao = int(c_VALOR_MAX_EDUCACAO * 100)
c_VALOR_MAX_TRANSPORTE = .15
porcentagem_transporte = int(c_VALOR_MAX_TRANSPORTE * 100)

def valida_gastos(moradia, porcentagem_moradia):
  if float(moradia) > porcentagem_moradia:
    print(f"Portanto, idealmente, o máximo de sua renda comprometida com moradia deveria ser de R$ {str(renda_mensal * c_VALOR_MAX_MORADIA).replace('.0', '')}.")
  else:
    print("Seus gastos estão dentro da margem recomendada.")

def orcamento_domestico(renda_mensal, gasto_moradia, gasto_educacao, gasto_transporte):
  moradia = str(gasto_moradia * 100 / renda_mensal).replace('.0', '')
  educacao = str(gasto_educacao * 100 / renda_mensal).replace('.0', '')
  transporte = str(gasto_transporte * 100 / renda_mensal).replace('.0', '')

  print(f"\nDiagnóstico:\nSeus gastos totais com moradia comprometem {moradia}% de sua renda total. O máximo recomendado é de {porcentagem_moradia}%.", end=" ")
  valida_gastos(moradia, porcentagem_moradia)
  print(f"Seus gastos totais com educação comprometem {educacao}% de sua renda total. O máximo recomendado é de {porcentagem_educacao}%.", end=" ")
  valida_gastos(educacao, porcentagem_educacao)
  print(f"Seus gastos totais com transporte comprometem {transporte}% de sua renda total. O máximo recomendado é de {porcentagem_transporte}%.", end=" ")
  valida_gastos(transporte, porcentagem_transporte)

renda_mensal = float(input("Renda mensal total: R$ "))
gasto_moradia = float(input("Gastos totais com moradia: R$ "))
gasto_educacao = float(input("Gastos totais com educação: R$ "))
gasto_transporte = float(input("Gastos totais com transporte: R$ "))
orcamento_domestico(renda_mensal, gasto_moradia, gasto_educacao, gasto_transporte)