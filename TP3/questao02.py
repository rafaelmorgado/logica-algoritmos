def eleitor_obrigatorio(idade_eleitor):
  if idade_eleitor <= 0:
    print("Idade precisa ser maior que 0.")
  elif 0 < idade_eleitor < 16:
    print("Não tem direito a voto.")
  elif 16 <= idade_eleitor < 18 or idade_eleitor >= 70:
      print("Não tem obrigação de votar.")
  else:
    print("Tem obrigação de votar.")

idade_eleitor = int(input("Informe a idade: "))
eleitor_obrigatorio(idade_eleitor)