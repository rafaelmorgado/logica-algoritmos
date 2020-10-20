''' 17) Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120 '''

fatorial = 1
num = int(input("Entre com um número: "))

for x in range(num, 1, -1):
  fatorial = fatorial*x
print(f"{num:d}! = {fatorial:d}")