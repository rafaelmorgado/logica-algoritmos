''' 37) Uma academia deseja fazer um senso entre seus clientes para descobrir o mais alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um programa que pergunte a cada um dos clientes da academia seu código, sua altura e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0 (zero) no campo código. Ao encerrar o programa também deve ser informados os códigos e valores do clente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes '''
cliente = 1
print("Cliente: ", cliente)
altura = float(input("Entre com a altura: "))
peso = float(input("Entre com o peso: "))

altura_maior = altura_menor = altura
peso_maior = peso_menor = peso
cliente_maior_altura = cliente_menor_altura = cliente
cliente_maior_peso = cliente_menor_peso = cliente


while altura != 0 and peso != 0:
  if altura > altura_maior:
    altura_maior = altura
    cliente_maior_altura = cliente
  if altura < altura_menor:
    altura_menor = altura
    cliente_menor_altura = cliente
  if peso > peso_maior:
    peso_maior = peso
    cliente_maior_peso = cliente
  if peso < peso_menor:
    peso_menor = peso
    cliente_menor_peso = cliente
  if altura == 0 and peso == 0:
    break
  cliente += 1
  print("Cliente: ", cliente)
  altura = float(input("Entre com a altura: "))
  peso = float(input("Entre com o peso: "))

print(f"\n{cliente_maior_altura} é o mais alto com: {altura_maior}")
print(f"{cliente_menor_altura} é o mais baixo com: {altura_menor}")
print(f"{cliente_maior_peso} é o mais gordo com: {peso_maior}")
print(f"{cliente_menor_peso} é o mais magro com: {peso_menor}")
