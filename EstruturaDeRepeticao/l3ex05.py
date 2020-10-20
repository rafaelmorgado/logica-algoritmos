''' 5) Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. Valide a entrada e permita repetir a operação. '''

anos = 0

populacao_A = float(input("Total de habitantes da população A:"))
while populacao_A <= 0:
  print("Erro:")
  populacao_A = float(input("Total de habitantes da população A:"))

tx_crescimento_A = float(input("Taxa de crescimento da população A:"))
while tx_crescimento_A <= 0:
  print("Erro:")
  tx_crescimento_A = float(input("Taxa de crescimento da população A:"))

populacao_B = float(input("Total de habitantes da população B:"))
while populacao_B <= 0:
  print("Erro:")
  populacao_B = float(input("Total de habitantes da população B:"))

tx_crescimento_B = float(input("Taxa de crescimento da população B:"))
while tx_crescimento_B <= 0:
  print("Erro:")
  tx_crescimento_B = float(input("Taxa de crescimento da população B:"))

while populacao_A <= populacao_B:
  populacao_A *= tx_crescimento_A
  populacao_B *= tx_crescimento_B
  anos = anos + 1

print(anos, "anos necessários, para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.")