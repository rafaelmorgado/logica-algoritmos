tabuleiro_jogador1 = [ [ ' ', ' ', ' ', ' ' ],
                       [ ' ', ' ', 'B', 'B' ],
                       [ ' ', ' ', ' ', ' ' ],
                       [ 'B', ' ', ' ', ' ' ],
                       [ 'B', ' ', ' ', 'B' ] ]

tabuleiro_jogador2 = [ [ ' ', ' ', ' ', ' ' ],
                       [ ' ', ' ', 'B', 'B' ],
                       [ ' ', ' ', ' ', ' ' ],
                       [ ' ', 'B', ' ', ' ' ],
                       [ '', 'B', ' ', 'B' ] ]
jogadores = 2
acertos = 0

for jogador in range(jogadores):
  print(f"Jogador {jogador+1}:")
  print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in tabuleiro_jogador1]))
  for tiros in range(5):
    linha = int(input("Em qual linha deseja atirar: "))
    coluna = int(input("Em qual coluna deseja atirar: "))

    while 0 <= jogador <= linha and 0 <= tiros <= coluna:
      if tabuleiro_jogador1[linha][coluna] == 'B':
        acertos += 1
      tabuleiro_jogador1[linha][coluna] = 'X'
      print('\n'.join([''.join(['{:4}'.format(item) for item in row]) 
      for row in tabuleiro_jogador1]))
      break

      if tabuleiro_jogador2[linha][coluna] == 'B':
        acertos += 1
      tabuleiro_jogador1[linha][coluna] = 'X'
      print(tabuleiro_jogador2)
      break
    else:
      print("Erro")

    print(f"\nJogador {jogador+1} acertou!!!!")
  acertos = 0