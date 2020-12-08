def divisao_conta(total_conta, pessoas, perc_servico):
  if pessoas > 0:
    if 0 <= perc_servico <= 100:
      valor_servico = (total_conta * perc_servico) / 100
      divisao_conta = (total_conta+valor_servico) / pessoas
      print(f"O valor total da conta, com a taxa de serviço, será de R$ {str(divisao_conta.__format__('.2f')).replace('.', ',')}.")

vl_total_consumo = float(input("Informe o valor total do consumo: R$ "))
nmr_pessoas = int(input("Informe o total de pessoas: "))
percent_servico = float(input("Informe o percentual do serviço, entre 0 e 100: "))
divisao_conta(vl_total_consumo, nmr_pessoas, percent_servico)