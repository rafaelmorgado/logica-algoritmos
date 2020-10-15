''' 9) Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9). '''

temperatura = float(input("Entre com a temperatura: "))
temperatura_c = 5 *((temperatura-32) / 9)

print("Temperatura: %.2f" % temperatura_c, "c")