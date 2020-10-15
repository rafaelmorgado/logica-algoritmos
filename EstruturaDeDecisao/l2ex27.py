''' 27) Uma fruteira está vendendo frutas com a seguinte tabela de preços:
                      Até 5 Kg           Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg
Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg
Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar R$ 25,00, receberá ainda um desconto de 10% sobre este total. Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) de maças adquiridas e escreva o valor a ser pago pelo cliente. '''

fruta = str(input("G-Morango, A-Maçã: ").upper())
quantidade = float(input("Informe a quantidade: "))

if quantidade > 0:
  if fruta == 'G' or 'A':
    if fruta == 'G':
      if quantidade <= 5:
        preco = quantidade * 2.50
        print("Preço: R$ %.2f" % preco)
      elif quantidade > 5 and quantidade <= 8:
        preco = quantidade * 2.20
        print("Preço: R$ %.2f" % preco)
      else:
        preco = (quantidade * 2.20)
        if preco > 25:
          desconto = preco * .10
          preco -= desconto
          print("Preço: R$ %.2f" % preco)
        else:
          print("Preço: R$ %.2f" % preco)
    if fruta == 'A':
      if quantidade > 0 and quantidade <= 5:
        preco = quantidade * 1.80
        print("Preço: R$ %.2f" % preco)
      elif quantidade > 5 and quantidade <= 8:
        preco = quantidade * 1.50
        print("Preço: R$ %.2f" % preco)
      else:
        preco = (quantidade * 1.50)
        if preco > 25:
          desconto = preco * .10
          preco -= desconto
          print("Preço: R$ %.2f" % preco)
        else:
          print("Preço: R$ %.2f" % preco)
    else:
      print("\nERRO: Dado inválido\nEscolha: G-Morango ou A-Maçã")
else:
  print("Quantidade tem que ser maior que 0")