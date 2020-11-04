def desenha_losango(altura):
  print("Losango: \n")
  for x in range(1, altura, 2):
      print(('#' * x).center(altura, ' '))
  if altura % 2 == 0:
    for x in range(altura-3, 0, -2):
      print(('#' * x).center(altura, ' '))
  else:
    for x in range(altura-4, 0, -2):
      print(('#' * x).center(altura, ' '))

altura = int(input("Entre com a altura do losango: "))
if altura >= 4:
    desenha_losango(altura)
else:
    print("\nErro: Impossível desenhar o losango.\nAltura precisar ser maior ou igual a 4.")