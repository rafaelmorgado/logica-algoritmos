''' 21) Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. '''

NOTAS_100 = 100
NOTAS_50 = 50
NOTAS_10 = 10
NOTAS_5 = 5
NOTAS_1 = 1

saque = float(input("Entre com o valor do saque: "))

if saque >= 10 and saque <= 600:
  if saque % 100 >= 0:
    n100 = saque // NOTAS_100
    saque -= n100 * NOTAS_100
    print(f"{n100:.0f} nota(s) de R$ 100,00\n")
  if saque % 50 >= 0:
    n50 = saque // NOTAS_50
    saque -= n50*NOTAS_50
    print(f"{n50:.0f} nota(s) de R$ 50,00\n")
  if saque % 10 >= 0:
    n10 = saque // NOTAS_10
    saque -= n10*NOTAS_10
    print(f"{n10:.0f} nota(s) de R$ 10,00\n")
  if saque % 5 >= 0:
    n5 = saque // NOTAS_5
    saque -= n5*NOTAS_5
    print(f"{n5:.0f} nota(s) de R$ 5,00\n")
  if saque % 1 >= 0:
    n1 = saque // NOTAS_1
    saque -= n1*NOTAS_1
    print(f"{n1:.0f} nota(s) de R$ 1,00\n")
else:
  print("Valor maior que R% 600.00 ou menor que R$ 10.00")