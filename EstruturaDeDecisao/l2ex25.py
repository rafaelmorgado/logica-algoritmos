''' 25) Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" 
O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente". '''

resposta_sim = 0
resposta1 = str(input("Telefonou para a vítima? ").upper())
resposta2 = str(input("Esteve no local do crime? ").upper())
resposta3 = str(input("Mora perto da vítima? ").upper())
resposta4 = str(input("Devia para a vítima? ").upper())
resposta5 = str(input("Já trabalhou com a vítima? ").upper())

if resposta1 == 'SIM':
  resposta_sim += 1

if resposta2 == 'SIM':
  resposta_sim += 1

if resposta3 == 'SIM':
  resposta_sim += 1

if resposta4 == 'SIM':
  resposta_sim += 1

if resposta5 == 'SIM':
  resposta_sim += 1

if resposta_sim == 2:
  print("Suspeita")
elif resposta_sim == 3 and resposta_sim == 4:
  print("Cúmplice")
elif resposta_sim == 5:
  print("Assassino")
else:
  print("Inocente")
  print(resposta_sim)