''' 44) Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:

1 , 2, 3, 4  - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
O total de votos para cada candidato;
O total de votos nulos;
O total de votos em branco;
A percentagem de votos nulos sobre o total de votos;
A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero. '''

total_votos = cont1 = cont2 = cont3 = cont4 = cont5 = cont6 = 0

print("Candidatos:\n1 - Jose\n2 - João\n3 - Pedro\n4 - Plinio\n5 - Voto Nulo\n6 - Voto em Branco\n")
voto = int(input("voto: "))
while voto > 0:
    if voto == 1:
        cont1 += 1
        total_votos += cont1
    if voto == 2:
        cont2 += 1
        total_votos += cont2
    if voto == 3:
        cont3 += 1
        total_votos += cont3
    if voto == 4:
        cont4 += 1
        total_votos += cont4
    if voto == 5:
        cont5 += 1
    if voto == 6:
        cont6 += 1
    voto = int(input("voto: "))

percentagem_votos_nulos = (cont5 / total_votos) * 100
percentagem_votos_brancos = (cont6 / total_votos) * 100

print(f"\ntotal votos para o Jose: {cont1}")
print(f"total votos para o João: {cont2}")
print(f"total votos para o Pedro: {cont3}")
print(f"total votos para o Plínio: {cont4}")
print(f"total votos nulo: {cont5}")
print(f"total votos em branco: {cont6}")
print(f"percentagem de votos nulos: {percentagem_votos_nulos:.2f}%")
print(f"percentagem de votos branco: {percentagem_votos_brancos:.2f}%")