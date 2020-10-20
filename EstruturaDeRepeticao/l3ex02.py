''' 2) Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. '''

usuario = str(input("Entre com um usuário: ").upper())
senha = str(input("Entre com um senha: ").upper())

while usuario == senha:
  print("Usuário/Senha não podem ser iguais.")
  usuario = str(input("Entre com um usuário: ").upper())
  senha = str(input("Entre com um senha: ").upper())
else:
  print("Usuário cadastrado com sucesso!")
