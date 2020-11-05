''' 4) Está nos SLIDES, feito em sala: Escreva um algoritmo para motivação do corpo discente. Ele deve pedir a nota do aluno e em seguida apresentar uma mensagem para o usuário: • “Que Vergonha!” Caso a nota seja 0 • “Precisa estudar muito mais!” Caso a nota seja maior que 0 e menor que 5 • “Tem que estudar mais...” Caso a nota seja maior ou igual a 5 e menor que 8 • “Falta pouco!” Caso a nota seja maior ou igual a 8 e menor que 10 • “Parabéns! =)” Caso a nota seja 10 '''

nota = float(input("Entre com a nota: "))

if nota == 0:
  print("Que Vergonha!")
if nota > 0 and nota <= 5:
  print("Precisa estudar muito mais!")
if nota > 5 and nota <= 8:
  print("Falta pouco!")
if nota > 8 and nota <= 10:
  print("“Parabéns!")