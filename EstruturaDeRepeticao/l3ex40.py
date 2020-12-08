''' 40) Foi feita uma estatística em cinco cidades brasileiras para coletar dados sobre acidentes de trânsito. Foram obtidos os seguintes dados:
a.Código da cidade;
b.Número de veículos de passeio (em 1999);
c.Número de acidentes de trânsito com vítimas (em 1999). Deseja-se saber:
d.Qual o maior e menor índice de acidentes de transito e a que cidade pertence;
e.Qual a média de veículos nas cinco cidades juntas;
f.Qual a média de acidentes de trânsito nas cidades com menos de 2.000 veículos de passeio. '''

print("\nCidade:")
cod_cidade = int(input("Cod cidade: "))
total_veiculos_passeio = int(input("Total veiculos passeio: "))
total_acidentes_vitimas = int(input("Total acidentes vítima: "))

soma_acidentes = soma_veiculos = 0
cidades = 6

total_mais_veiculos = total_menos_veiculos = total_veiculos_passeio
cidade_mais_veiculos = cidade_menos_veiculos = cod_cidade

total_mais_vitimas = total_menos_vitimas = total_acidentes_vitimas
cidade_mais_vitimas = cidade_menos_vitimas = cod_cidade

while cidades >= 0:
  cidades -= 1
  while total_veiculos_passeio >= 0 and total_acidentes_vitimas >= 0:
    if total_veiculos_passeio > total_mais_veiculos:
      total_mais_veiculos = total_veiculos_passeio
      cidade_mais_veiculos = cod_cidade
      soma_veiculos += total_veiculos_passeio
      break
    if total_veiculos_passeio < total_menos_veiculos:
      total_menos_veiculos = total_veiculos_passeio
      cidade_menos_veiculos = cod_cidade
      soma_veiculos += total_veiculos_passeio
      break
    if total_acidentes_vitimas > total_mais_vitimas:
      total_mais_vitimas = total_acidentes_vitimas
      cidade_mais_vitimas = cod_cidade
      soma_acidentes += total_acidentes_vitimas
      break
    if total_acidentes_vitimas < total_menos_vitimas:
      total_menos_vitimas = total_acidentes_vitimas
      cidade_menos_vitimas = cod_cidade
      soma_acidentes += total_acidentes_vitimas
      break
    print("\nCidade:")
    cod_cidade = int(input("Cod cidade: "))
    total_veiculos_passeio = int(input("Total veiculos passeio: "))
    total_acidentes_vitimas = int(input("Total acidentes vítima: "))
    break

media_veiculos = soma_veiculos / 5
media_acidentes = soma_acidentes / 5
print(f"\nCidade: código {cidade_mais_veiculos}, possui mais veículos")
print(f"Cidade: código {cidade_menos_veiculos}, possui menos veículos")
print(f"Cidade: código {cidade_mais_vitimas}, possui mais vítimas")
print(f"Cidade: código {cidade_menos_vitimas}, possui menos vítimas")
print(f"Média de veículos entre as 5 cidades: {media_veiculos}")
print(f"Média de acidentes entre as 5 cidades: {media_acidentes}")