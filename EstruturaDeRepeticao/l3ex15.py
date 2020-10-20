''' 15) A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. '''

n = int(input("Escolha o n−ésimo termo da série de Fibonacci: "))
anterior = 0
atual = 1
proximo = 0

print(anterior)
print(atual)
for x in range(1, n):
  if x > 1:
    proximo = atual + anterior
    anterior = atual
    atual = proximo
    print(proximo)