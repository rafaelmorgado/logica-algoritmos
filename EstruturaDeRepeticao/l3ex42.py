''' 42) Faça um programa que leia uma quantidade indeterminada de números positivos e conte quantos deles estão
 nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-100]. A entrada de dados deverá terminar quando for lido um número negativo. '''

cont_0_25 = cont_26_50 = cont_51_75 = cont_76_100 = 0

print("Informe apenas números positivos entre (0-100):")
numero = int(input("Entre com um número: "))
while 0 <= numero <= 100:
    if 0 <= numero <= 25:
        cont_0_25 += 1
    if 26 <= numero <= 50:
        cont_26_50 += 1
    if 51 <= numero <= 75:
        cont_51_75 += 1
    if 76 <= numero <= 100:
        cont_76_100 += 1
    numero = int(input("Entre com um número: "))
else:
    print(f"\nFim do programa: -> Número: {numero}\nO número precisa estar entre [0-100]")

print(f"\nTotais de números entre [0-25] = {cont_0_25}")
print(f"Totais de números entre [26-50] = {cont_26_50}")
print(f"Totais de números entre [51-75] = {cont_51_75}")
print(f"Totais de números entre [76-100] = {cont_76_100}")