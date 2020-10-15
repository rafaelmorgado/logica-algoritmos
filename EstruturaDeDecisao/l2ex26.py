''' 26) Um posto está vendendo combustíveis com a seguinte tabela de descontos:
Álcool:
até 20 litros, desconto de 3% por litro
acima de 20 litros, desconto de 5% por litro
Gasolina:
até 20 litros, desconto de 4% por litro
acima de 20 litros, desconto de 6% por litro Escreva um algoritmo que leia o número de litros vendidos, o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. '''

PRECO_ALCOOL = 1.90
PRECO_GASOLINA = 2.50

combustivel = str(input("A-álcool, G-gasolina ").upper())
litros = float(input("Informe a quantidade: ").upper())

if combustivel == 'A':
  if litros <= 20:
    desconto_alcool = PRECO_ALCOOL * 1.03
    preco_final = litros / desconto_alcool
    print(f"Preço: R$ {preco_final:.2f}")
  else:
    desconto_alcool = PRECO_ALCOOL * 1.05
    preco_final = litros / desconto_alcool
    print(f"Preço: R$ {preco_final:.2f}")

if combustivel == 'B':
  if litros <= 20:
    desconto_alcool = PRECO_ALCOOL * .04
    preco_final = litros / desconto_alcool
    print(f"Preço: R$ {preco_final:.2f}")
  else:
    desconto_alcool = PRECO_ALCOOL * .06
    preco_final = litros / desconto_alcool
    print(f"Preço: R$ {preco_final:.2f}")
