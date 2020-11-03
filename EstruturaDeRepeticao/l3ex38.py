''' 38) Um funcionário de uma empresa recebe aumento salarial anualmente: Sabe-se que:
Esse funcionário foi contratado em 1995, com salário inicial de R$ 1.000,00;
Em 1996 recebeu aumento de 1,5% sobre seu salário inicial;
A partir de 1997 (inclusive), os aumentos salariais sempre correspondem ao dobro do percentual do ano anterior. Faça um programa que determine o salário atual desse funcionário. Após concluir isto, altere o programa permitindo que o usuário digite o salário inicial do funcionário. '''

# salario = float(input("Entre com o salário: "))
salario = 1000
ano = 1995
percentual_aumento = .015
percentual_aumento_recalculado_2 = percentual_aumento_recalculado = novo_salario = ano_salario = 0

ano_requisitado = int(input("Entre com o ano: "))

for x in range(ano, ano_requisitado+1):
  if ano >= 1997:
    percentual_aumento_recalculado += percentual_aumento_recalculado * 2 - percentual_aumento_recalculado
    salario_reajustado = salario * percentual_aumento_recalculado
    novo_salario = salario + salario_reajustado
    print(f"{ano} -> {novo_salario:.2f} - {percentual_aumento_recalculado*100}%")
    ano += 1
  else:
    percentual_aumento_recalculado = percentual_aumento * (ano - 1995)
    salario_reajustado = salario * percentual_aumento_recalculado
    novo_salario = salario + salario_reajustado
    print(f"{ano} -> {novo_salario:.2f} - {percentual_aumento_recalculado*100}%")
    ano += 1
