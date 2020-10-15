''' 18) Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a mesma é uma data válida. '''

dia = int(input("Introduza uma dia: "))
mes = int(input("Introduza uma mês: "))
ano = int(input("Introduza uma ano: "))

if mes == 4 or mes == 6 or mes == 9 or mes == 11:
  if dia >= 1 and dia <= 30:
    print("Data válida")
  else:
    print("Data inválida")
elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
  if dia >= 1 and dia <= 31:
    print("Data válida")
  else:
    print("Data inválida")
elif mes == 2:
  if ano % 4 == 0:
    if dia >= 1 and dia <= 29:
      print("Data válida")
    else:
      print("Data inválida")
  else:
    if dia >= 1 and dia <= 28:
      print("Data valida")
    else:
      print("Data invalida")
else:
  print("Mês inválido")