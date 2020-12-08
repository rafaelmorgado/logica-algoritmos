def concurso():
  notas = {}
  for aluno in range(5):
    nome = str(input(f"Informe nome do {aluno+1}º participante: "))
    nota = float(input(f"Informe nota do {aluno+1}º participante: "))
    while nota < 0 or nota > 10:
      print("Nota precisa estar entre(0-10)")
      nota = float(input(f"Informe nota do {aluno + 1}º participante: "))
    else:
      notas.__setitem__(nome, nota)
  lista_notas = notas.values()
  maior_nota = max(lista_notas)
  for key, value in notas.items():
    if maior_nota:
      aluno = key
      maior_nota = value
  print(f"\nO(a) vencedor(a) foi {aluno} com nota {maior_nota}!")

concurso()