''' 3) Faça um programa que leia e valide as seguintes informações:
-> Nome: maior que 3 caracteres;
-> Idade: entre 0 e 150;
-> Salário: maior que zero;
-> Sexo: 'f' ou 'm';
-> Estado Civil: 's', 'c', 'v', 'd'; '''

nome = str(input("Entre com o nome: ").upper())
while len(nome) <= 3:
  print("Erro: nome menor que 3: ")
  nome = str(input("Entre com o nome: "))

idade = int(input("Entre com o a idade: "))
while idade < 0 or idade > 150:
  if idade < 0:
    print("Erro: Idade menor que 0")
    idade = int(input("Entre com o a idade: "))
  else:
    print("Erro: Idade maior que 150")
    idade = int(input("Entre com o a idade: "))

salario = float(input("Entre com o salário R$: "))
while salario <= 0:
  print("Erro: Salário menor que 0")
  salario = float(input("Entre com o salário R$: "))

sexo = str(input("Entre com o sexo: ").upper())
while sexo != 'F' and sexo != 'M':
  print("Erro: sexo inválido: ")
  sexo = str(input("Entre com o sexo: ").upper())

estado_civil = str(input("Entre com o estado civil: ").upper())
while estado_civil != 'S' and estado_civil != 'C' and estado_civil != 'V' and estado_civil != 'D':
  print("Erro: estado civil inválido: ")
  sexo = str(input("Entre com o sexo: ").upper())

print("\nNome: ", nome)
print("Idade: %d" % idade)
print("Salário R$: %.2f " % salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)