''' 4) Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0. '''

aluno_notas = []
notas = []
media_notas = []
soma_notas = media = 0

for aluno in range(1, 3):
  print(f"Aluno {aluno}:")
  for nota in range(1, 5):
    notas.append(float(input(f"{nota}º nota: ")))
    soma_notas += notas[nota-1]
  aluno_notas.append(notas[aluno])
  media = soma_notas / 4
  media_notas.append(media)
  soma_notas = 0

print(aluno_notas)
print(media_notas)

    # names = list(set([i[0] for i in data])) 
    # consolidated = [] # empty list to get the sublists

    # # Looping for each name
    # for name in names:
    #     subList = [name] # sublist for each name
    #     for i in data: # loop for each item within data_list
    #         if i[0] == name: # if name is the same, append the subject
    #             subList.append(i[1])
    #     consolidated.append(subList) # append sublists in consolidated list
    # return consolidated