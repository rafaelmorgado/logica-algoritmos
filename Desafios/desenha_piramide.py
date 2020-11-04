def desenha_piramide(altura):
  print("Pirâmide: \n")
  for x in range(1, altura, 2):
      print(('#' * x).center(altura, ' '))

altura = int(input("Entre com a altura da pirâmide: "))
if altura >= 4:
    desenha_piramide(altura)
else:
    print("\nErro: Impossível desenhar a pirâmide.\nAltura precisar ser maior ou igual a 4.")