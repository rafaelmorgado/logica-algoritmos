''' 28) O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
                      Até 5 Kg           Acima de 5 Kg
File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
Para atender a todos os clientes, cada cliente poderá levar apenas um dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente. Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra. Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar. '''

fruta = str(input("F-Filé Duplo, A-Alcatra, P-Picanha: ").upper())
quantidade = float(input("Informe a quantidade: "))
cartao_tabajara = str(input("Compra com Cartão Tabajara: (S-Sim ou N-Não): ").upper())

if quantidade > 0:
  if cartao_tabajara == 'S':
    if fruta == ('F' or 'A' or 'P'):
      if fruta == 'F':
        if quantidade <= 5:
          preco = quantidade * 4.90
          desconto = preco * .05
          preco -= desconto
          print("Preço: R$ %.2f" % preco)
        elif quantidade > 5:
          preco = quantidade * 5.80
          desconto = preco * .05
          preco -= desconto
          print("Preço: R$ %.2f" % preco)
      if fruta == 'A':
        if quantidade <= 5:
          preco = quantidade * 5.90
          desconto = preco * .05
          preco -= desconto
          print("Preço: R$ %.2f" % preco)
        elif quantidade > 5:
          preco = quantidade * 6.80
          desconto = preco * .05
          preco -= desconto
          print("Preço: R$ %.2f" % preco)
      if fruta == 'P':
        if quantidade <= 5:
          preco = quantidade * 6.90
          desconto = preco * .05
          preco -= desconto
          print("Preço: R$ %.2f" % preco)
        elif quantidade > 5:
          preco = quantidade * 7.80
          desconto = preco * .05
          preco -= desconto
          print("Preço: R$ %.2f" % preco)
    else:
      print("\nERRO: Dado inválido\nEscolha: G-Morango ou A-Maçã")
  elif cartao_tabajara == 'N':
    if fruta == ('F' or 'A' or 'P'):
      if fruta == 'F':
        if quantidade <= 5:
          preco = quantidade * 4.90
          print("Preço: R$ %.2f" % preco)
        elif quantidade > 5:
          preco = quantidade * 5.80
          print("Preço: R$ %.2f" % preco)
      if fruta == 'A':
        if quantidade <= 5:
          preco = quantidade * 5.90
          print("Preço: R$ %.2f" % preco)
        elif quantidade > 5:
          preco = quantidade * 6.80
          print("Preço: R$ %.2f" % preco)
      if fruta == 'P':
        if quantidade <= 5:
          preco = quantidade * 6.90
          print("Preço: R$ %.2f" % preco)
        elif quantidade > 5:
          preco = quantidade * 7.80
          print("Preço: R$ %.2f" % preco)
    else:
      print("\nERRO: Escolha: F-Filé Duplo, A-Alcatra, P-Picanha")
  else:
    print("Comando inválido. Escolha: (S-Sim ou N-Não")
else:
  print("Quantidade tem que ser maior que 0")