''' 4) Faça um Programa que verifique se uma letra digitada é vogal ou consoante. '''

letra = str(input("Insira uma letra: ").upper())

if letra == 'A' and 'E' and 'I' and 'O' and 'U':
  print(letra, "é vogal")
else:
  print(letra, "é consoante")