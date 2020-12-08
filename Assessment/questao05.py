import matplotlib.pyplot as plt
import replit

class Pib:
  def __init__(self):
    self.ano = 0
    self.valor = 0

class Pais:
  def __init__(self, nome):
    self.nome = nome
    self.pibs = {}

paises = []

def retorno_menu_buscar_pib():
  op_voltar = str(input("\nDigite: \"sim\", para nova consulta.\nou use qualquer tecla para volar ao menu.\n").upper())
  if op_voltar == "SIM" or op_voltar == 'S':
    replit.clear()
    buscar_pib(paises)
  else:
    replit.clear()
    menu()

def retorno_estimativa_pib():
  op_voltar = str(input("\nUse qualquer tecla para volar ao menu...\n"))
  if len(op_voltar) >= 0:
    replit.clear()
    menu()

# abrir o CSV
def abrir_arquivo():
  arquivo = open("Assessment/arquivoqt05.csv", "r")  
  conteudo = arquivo.read()
  linhas = conteudo.split('\n')
  for i in range(1, len(linhas)):
    dados = linhas[i].split('\t')
    anos = linhas[0].split('\t')
    pais = Pais(dados[0])
    for x in range(1, len(dados)):
      pib = Pib()
      pib.ano = anos[x]
      pib.valor = dados[x]
      pais.pibs.__setitem__(pib.ano, pib.valor)
    paises.append(pais)

# função que permite ao usuário solicitar o PIB de um país para um determinado ano.
def buscar_pib(paises):
  nome_pais = str(input("Informe um país: ").capitalize())
  for pais in paises:
    if pais.nome.capitalize() == nome_pais:
      if pais.nome.capitalize() == 'Eua':
        nome_pais = pais.nome.upper()
      ano_pib = int(input("Informe um ano entre 2013 e 2020: "))  
      if str(ano_pib) in pais.pibs:
        for ano, pib in pais.pibs.items():
          if ano == str(ano_pib):
            print(f"PIB {nome_pais} em {ano}: US${pib} trilhões.")
            retorno_menu_buscar_pib()
      else:
        print("\nAno não disponível.")
        retorno_menu_buscar_pib()
  else:
    print("\nPaís não disponível.")
    retorno_menu_buscar_pib()


# função que lista, por país, a estimativa de variação do PIB, em percentual, entre 2013 e 2020.
def estimativa_pib(paises):
  for pais in paises:
    for ano, pib in pais.pibs.items():
      if ano == '2013':
        vi = float(pib)
      if ano == '2020':
        vf = float(pib)
        variacao = (vf/vi-1)*100 #cálculo da variação percentual
        print(f"{pais.nome:20} Variação de {variacao:.2f}% entre 2013 e 2020.")
        break
  retorno_estimativa_pib()
        
# função que, para um país, exiba o gráfico da evolução do PIB ao longo dos anos.
def grafico_pib(paises):
  nome_pais = str(input("Informe um país: ").capitalize())
  for pais in paises:
    if pais.nome.capitalize() == nome_pais:
      if pais.nome.capitalize() == 'Eua':
        nome_pais = pais.nome.upper()  
      eixo_x = pais.pibs.keys()
      eixo_y = pais.pibs.values()
      plt.plot(eixo_x, eixo_y)
      plt.xlabel("Ano")
      plt.ylabel("Pib")
      plt.title(f"Evolução do Pib {nome_pais}")
      plt.show()

def menu():
  print('''
MENU:

[1] - Solicitar o PIB de um país para um determinado ano
[2] - Estimativa de variação do PIB, em percentual, dos países entre 2013 e 2020
[3] - Gráfico da evolução do PIB ao longo dos anos
[0] - Sair
''')

  opcao = int(input("Escolha uma opção: "))
  while opcao != 0:
    if opcao == 1:
      replit.clear()
      buscar_pib(paises)
      break
    if opcao == 2:
      replit.clear()
      estimativa_pib(paises)
      break
    if opcao == 3:
      replit.clear()
      grafico_pib(paises)
      break
    replit.clear()
    print("Erro: Opção inexistente! Tente novamente.")
    menu()  
  
abrir_arquivo()
menu()
print("Fim do programa!")