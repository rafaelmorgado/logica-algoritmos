import matplotlib.pyplot as plt
eixo_x = []
eixo_y = []

valor_inicial = float(input("Valor inicial: R$ "))
rendimento = float(input("Rendimento por período (%): "))
aporte = float(input("Aporte a cada período: R$ "))
periodos = int(input("Total de períodos: "))

montante = valor_inicial
for periodo in range(1, periodos+1):
  rendimento_periodo = montante * rendimento / 100
  montante += rendimento_periodo + aporte
  eixo_x.append(periodo)
  eixo_y.append(montante)
  print(f"Após {periodo} períodos(s), o montante será de R${montante:.2f}.")

plt.plot(eixo_x, eixo_y)
plt.xlabel("Período")
plt.ylabel("Redimento")
plt.title("Evolução do Valor Acumulado")
plt.show()