''' 17) Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto. '''

bissexto = int(input("Entre com o ano: "))

if bissexto % 400 == 0:
  print(bissexto,"é bissexto")
elif bissexto % 4 == 0 and bissexto % 100 != 0:
  print(bissexto,"é bissexto")
else:
  print(bissexto, "Não é bissexto")