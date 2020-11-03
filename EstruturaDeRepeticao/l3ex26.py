''' 26) Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato. '''

eleitores = int(input("Total de eleitores: "))

candidato_A = 'A'
candidato_B = 'B'
candidato_C = 'C'
qt_votos_A = qt_votos_B = qt_votos_C = 0

while eleitores > 0:
  voto = str(input("Entre com o voto: ").upper())
  while voto == 'A' or voto == 'B' or voto == 'C':
      if voto == candidato_A:
        qt_votos_A += 1
        eleitores -= 1
        break
      if voto == candidato_B:
        qt_votos_B += 1
        eleitores -= 1
        break
      if voto == candidato_C:
        qt_votos_C += 1
        eleitores -= 1
        break
  else:
      print("\nErro: Tente novamente! votos(A, B ou C)")

if qt_votos_A > qt_votos_B and qt_votos_A > qt_votos_C:
    print("Candidato A vencedor!")
elif qt_votos_B > qt_votos_A and qt_votos_B > qt_votos_C:
    print("Candidato B vencedor!")
elif qt_votos_C > qt_votos_B and qt_votos_C > qt_votos_A:
    print("Candidato C vencedor!")
else:
    print("Empate")