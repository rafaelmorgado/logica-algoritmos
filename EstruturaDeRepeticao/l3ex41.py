''' 41) Faça um programa que receba o valor de uma dívida e mostre uma tabela com os seguintes dados:
valor da dívida, valor dos juros, quantidade de parcelas e valor da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas  % de Juros sobre o valor inicial da dívida
1       0
3       10
6       15
9       20
12      25

Exemplo de saída do programa:

Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela
R$ 1.000,00     0               1                       R$  1.000,00
R$ 1.100,00     100             3                       R$    366,00
R$ 1.150,00     150             6                       R$    191,67 '''

divida = float(input("Informe o valor da dívida: "))

print("Valor da Dívida Valor dos Juros Quantidade de Parcelas  Valor da Parcela")
valor_parcela = juros = 0
x = 1

for parcela in range(1, 9, 3):
  if parcela > 1:
    parcela -= 1
    x += 1
    juros = 50 * x
    divida = divida + juros
    valor_parcela = divida / parcela
    print(f"{divida:<15} {juros:<15} {parcela:<23} R$ {valor_parcela:.2f}")
    divida = 1000
  else:
    valor_parcela = divida
    print(f"{divida:<15} {juros:<15} {parcela:<23} R$ {valor_parcela:.2f}")