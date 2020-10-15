''' 20) Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10. '''

n1 = float(input("Entre com a 1a nota: "))
n2 = float(input("Entre com a 2a nota: "))
n3 = float(input("Entre com a 3a nota: "))

media = (n1 + n2 + n3) / 3

if n1 <= 10 and n2 <= 10 and n3 <= 10:
  if media == 10:
    print("Aprovado com Distinção")
  elif media > 7:
    print("Aprovado")
  elif media >= 0 and media < 7:
    print("Reprovado")
else:
  print("Erro: Nota maior que 10")