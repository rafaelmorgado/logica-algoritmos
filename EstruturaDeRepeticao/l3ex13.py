''' 13) Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro número elevado ao segundo número. Não utilize a função de potência da linguagem. '''

resultado = 1

base = int(input("Entre com a base: "))
expoente = int(input("Entre com o expoente: "))

if expoente >= 2:
  for x in range(1, expoente+1):
    resultado *= base

if expoente == 1:
  base = base
  resultado = base

print("base:",base)
print(base,"^",expoente,"=",resultado)