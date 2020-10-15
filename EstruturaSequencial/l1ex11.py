''' 11) Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
-> o produto do dobro do primeiro com metade do segundo .
-> a soma do triplo do primeiro com o terceiro.
-> o terceiro elevado ao cubo. '''

print("Entre com 2 números inteiros: ")
n1 = int(input())
n2 = int(input())
print("Entre com número real: ")
n3 = float(input())

a = (n1*2) * (n2/2)
b = (n1*3) + n3
c = n3**3

print("a -> ", a)
print("b -> %.2f" % b)
print("c -> %.2f" % c)