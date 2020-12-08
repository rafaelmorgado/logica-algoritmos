jogo = [ [ ' ', ' ', ' ' ],
         [ ' ', ' ', ' ' ],
         [ ' ', ' ', ' ' ]]

def imprimir_tabuleiro():
  for jogador in range(2):
    print(f"Jogador {jogador+1}:")
    print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
        for row in jogo]))
    for tiros in range(5):
      linha = int(input("Em qual linha deseja atirar: "))
      coluna = int(input("Em qual coluna deseja atirar: "))
      jogo[linha][coluna] = 'X'
      print('\n'.join([''.join(['{:3}'.format(item) for item in row]) 
        for row in jogo]))

imprimir_tabuleiro()