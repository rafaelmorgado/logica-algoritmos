''' 24) Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
-> par ou ímpar;
-> positivo ou negativo;
-> inteiro ou decimal. '''

n1 = float(input("Entre com 1a número: "))
n2 = float(input("Entre com 2a número: "))
op = str(input("Entre com uma operação matemática: "))


if op == '+':
	resultado = n1 + n2
	if resultado % 2 == 0:
		print("O numero %d e par!" % resultado)
	else:
		print("O numero %d e impar." % resultado)
	if resultado >= 0:
		print("O numero %.2f e Positivo!" % resultado)
	else:
		print("O numero %.2f e negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d e inteiro!" % resultado)
	else:
		print("O numero %.2f e decimal." % resultado)

if op == '-':
	resultado = n1 - n2
	if resultado % 2 == 0:
		print("O numero %d e par!" % resultado)
	else:
		print("O numero %d e impar." % resultado)
	if resultado >= 0:
		print("O numero %.2f e Positivo!" % resultado)
	else:
		print("O numero %.2f e negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d e inteiro!" % resultado)
	else:
		print("O numero %.2f e decimal." % resultado)

if op == '*':
	resultado = n1 * n2
	if resultado % 2 == 0:
		print("O numero %d e par!" % resultado)
	else:
		print("O numero %d e impar." % resultado)
	if resultado >= 0:
		print("O numero %.2f e Positivo!" % resultado)
	else:
		print("O numero %.2f e negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d e inteiro!" % resultado)
	else:
		print("O numero %.2f e decimal." % resultado)

if op == '/':
	resultado = n1 / n2
	if resultado % 2 == 0:
		print("O numero %d e par!" % resultado)
	else:
		print("O numero %d e impar." % resultado)
	if resultado >= 0:
		print("O numero %.2f e Positivo!" % resultado)
	else:
		print("O numero %.2f e negativo." % resultado)
	if round(resultado) == resultado:
		print("O numero %d e inteiro!" % resultado)
	else:
		print("O numero %.2f e decimal." % resultado)