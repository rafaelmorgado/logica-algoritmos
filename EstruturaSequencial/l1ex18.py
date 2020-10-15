''' 18) Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
 '''

tamanho = float(input("Entre com o tamanho do arquivo: "))
velocidade_link = float(input("Entre com a velocidade do link: "))

tempo = (tamanho / (velocidade_link / 8)) / 60
print("Tempo: %.4f" % tempo)