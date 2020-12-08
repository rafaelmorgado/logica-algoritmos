''' 5) Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida.

FULANO
FULAN
FULA
FUL
FU
F '''

nome = str(input("Insira seu nome: ").upper())
for letra in range(len(nome)+1):
  print(nome[letra:])