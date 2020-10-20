''' 11) Altere o programa anterior para mostrar no final a soma dos números. '''

soma = 0
num1 = int (input("Entre com um número: "))
num2 = int (input("Entre com um número: "))

if num1 > num2:
  for x in range(num2, num1-1):
    print(x+1)
    soma += x+1
if num1 < num2:
  for x in range(num1, num2-1):
    print(x+1)
    soma += x+1
if num1 == num2:
  print("Erro: números iguais")

print("Soma:", soma)