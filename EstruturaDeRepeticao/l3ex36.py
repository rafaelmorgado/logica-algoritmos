''' 36) Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar em 10, o valor inicial e final devem ser informados também pelo usuário, conforme exemplo abaixo:
Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35 '''

num = int(input("Montar a tabuada de: "))
com = int(input("Começar por: "))
fim = int(input("Terminar em: "))

print("Tabuada de %d:"%num)
for x in range(com, fim+1):
  print(f"{num} X {x} = {num * x}")