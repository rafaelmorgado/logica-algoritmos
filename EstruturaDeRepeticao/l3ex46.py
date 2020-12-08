''' 46) Em uma competição de salto em distância cada atleta tem direito a cinco saltos. No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e depois informe a média dos saltos conforme a descrição acima informada (retirar o melhor e o pior salto e depois calcular a média). Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da execução, portanto não são ordenados. O programa deve ser encerrado quando não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m '''

resultados = []

saltos = {
  1: "Primeiro Salto",
  2: "Segundo Salto",
  3: "Terceiro Salto",
  4: "Quarto Salto",
  5: "Quinto Salto"
}

nome = str(input("Insira o nome do atleta: "))
while nome != '':
  print(f"Atleta: {nome}\n")
  for salto in range(1, 6):
    distancia = float(input(f"{saltos.get(salto)}: "))
    resultados.append(distancia)
  print(f"\nMelhor salto: {max(resultados)} m")
  resultados.remove(max(resultados))
  print(f"Pior salto: {min(resultados)} m")
  resultados.remove(min(resultados))
  soma = sum(resultados)
  media = soma / 3
  print(f"\nResultado final:\n{nome}: {media:.1f} m")
  nome = str(input("\nInsira o nome do atleta: "))
else:
  print("Fim do programa!")