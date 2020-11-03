''' 33) O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a maior temperaturas informadas, bem como a média das temperaturas. '''

print("Para finalizar o programa insira (x)")
temperatura = str(input("Entre com a temperatura: "))

TEMP_MAIOR = TEMP_MENOR = temperatura
cont = soma = 0
fim  = 'x'

while temperatura != fim:
  if temperatura > TEMP_MAIOR:
    TEMP_MAIOR = temperatura
  if temperatura < TEMP_MENOR:
    TEMP_MENOR = temperatura
  soma += float(temperatura)
  cont += 1
  if temperatura == 'x':
    break
  temperatura = str(input("Entre com a temperatura: "))

media = soma / cont
print("\nMaior:",TEMP_MAIOR)
print("Menor:",TEMP_MENOR)
print("Média das temperatura:",media)