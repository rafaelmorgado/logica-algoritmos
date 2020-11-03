''' 25) Faça um programa que peça para n pessoas a sua idade, ao final o programa devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada. '''

qt_pessoas = int(input("Entre com a quantidade de pessoas: "))

idades = cont = 0

while qt_pessoas > 0:
  idade = int(input("Insira sua idade: "))
  while 1 <= idade <= 120:
    idades += idade
    cont += 1
    qt_pessoas -= 1
    break
  else:
    print("\nErro: Tente novamente! notas entre(0-10)")

media_idades = idade / cont
if 0 <= media_idades <= 25:
  print("Turma é jovem")
if 26 <= media_idades <= 60:
  print("Turma é adulta")
if media_idades > 60:
  print("Turma é idosa")