''' 17) Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias. '''
import math

COBERTURA_LATA = 18 * 6
COBERTURA_GALAO = 3.6 * 6
PRECO_LATA = 80
PRECO_GALAO = 25

area = float(input("Informe a área do local: "))
litros = area / 6

latas = area / COBERTURA_LATA
galoes = area / COBERTURA_GALAO

qt_latas = (litros*1.1) // 18
m18 = litros%18
qt_galoes = math.ceil(m18/3.6)

print('\n')
preco_lata = math.ceil(latas)*PRECO_LATA
print ("Apenas lata(s):",math.ceil(latas))
print ("R$ %.2f" %preco_lata)
print('\n')
preco_galao = math.ceil(galoes)*PRECO_GALAO
print ("Apenas galõe(s):",math.ceil(galoes))
print ("R$ %.2f" %preco_galao)
print('\n')
preco_latas_e_galoes = ((qt_latas*PRECO_LATA)+(qt_galoes*PRECO_GALAO))
print("%d lata(s), %d galõe(s)" % (qt_latas,qt_galoes))
print ("R$ %.2f" %preco_latas_e_galoes) 