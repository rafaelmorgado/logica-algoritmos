''' 45) Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
Maior e Menor Acerto;
Total de Alunos que utilizaram o sistema;
A Média das Notas da Turma.
Gabarito da Prova:

01 - A
02 - B
03 - C
04 - D
05 - E
06 - E
07 - D
08 - C
09 - B
10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa. '''

gabarito = {
  1: 'A',
  2: 'B',
  3: 'C',
  4: 'D',
  5: 'E',
  6: 'E',
  7: 'C',
  8: 'D',
  9: 'B',
  10: 'A'
}
print(gabarito)

acertos = erros = 0

for questao in range(1, 11):
  resposta = str(input(f"Resposta questão {questao}: ").upper())
  resposta_gabarito = gabarito.get(questao)
  if resposta == resposta_gabarito:
    acertos += 1
    print("Acertou!")
  else:
    erros += 1
    print("Errrou!")

print(f"Acertos: {acertos}")