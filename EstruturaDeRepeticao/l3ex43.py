''' 43) O cardápio de uma lanchonete é o seguinte:
Especificação   Código  Preço
Cachorro Quente 100     R$ 1,20
Bauru Simples   101     R$ 1,30
Bauru com ovo   102     R$ 1,50
Hambúrguer      103     R$ 1,20
Cheeseburguer   104     R$ 1,30
Refrigerante    105     R$ 1,00
Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. Calcule e mostre o valor a ser pago
por item (preço * quantidade) e o total geral do pedido. Considere que o cliente deve informar quando o pedido deve
ser encerrado. '''

print("\nEspecificação   Código  Preço\n" +
"Cachorro Quente 100     R$ 1,20\n" +
"Bauru Simples   101     R$ 1,30\n" +
"Bauru com ovo   102     R$ 1,50\n" +
"Hambúrguer      103     R$ 1,20\n" +
"Cheeseburguer   104     R$ 1,30\n" +
"Refrigerante    105     R$ 1,00")

fim = 'SIM'
fim_resposta = ''
cont100 = cont101 = cont102 = cont103 = cont104 = cont105 = total_pedido = 0
total100 = total101 = total102 = total103 = total104 = total105 = 0
while fim_resposta != fim:
    codigo_item = int(input("\nEntre com código do produto: "))
    while 100 <= codigo_item <= 105:
        quantidade = int(input("Entre com a quantidade: "))
        if quantidade > 0:
            if codigo_item == 100:
                total100 += 1.2 * quantidade
                total_pedido += total100
                cont100 += quantidade
            if codigo_item == 101:
                total101 += 1.3 * quantidade
                total_pedido += total101
                cont101 += quantidade
            if codigo_item == 102:
                total102 += 1.3 * quantidade
                total_pedido += total102
                cont102 += quantidade
            if codigo_item == 103:
                total103 += 1.3 * quantidade
                total_pedido += total103
                cont103 += quantidade
            if codigo_item == 104:
                total104 += 1.3 * quantidade
                total_pedido += total104
                cont104 += quantidade
            if codigo_item == 105:
                total105 += 1.3 * quantidade
                total_pedido += total105
                cont105 += quantidade
            fim_resposta = str(input("Digite (sim) se deseja encerrar o pedido: ").upper())
            break
        else:
            print("\nErro: Tente novamente!\nQuantidade precisa ser maior que 0!")
    else:
        print("\nErro: Tente novamente!\nCódigo precisa estar entre (100-105)!")

print(f"\nEspecificação   Código  Preço   Qtd.   Total\n" +
f"Cachorro Quente 100     R$ 1,20   {cont100}    R$ {total100:.2f}\n" +
f"Bauru Simples   101     R$ 1,30   {cont101}    R$ {total101:.2f}\n" +
f"Bauru com ovo   102     R$ 1,50   {cont102}    R$ {total102:.2f}\n" +
f"Hambúrguer      103     R$ 1,20   {cont103}    R$ {total103:.2f}\n" +
f"Cheeseburguer   104     R$ 1,30   {cont104}    R$ {total104:.2f}\n" +
f"Refrigerante    105     R$ 1,00   {cont105}    R$ {total105:.2f}\n" +
"______________________________________________"
f"\nTotal dos produstos                    R$ {total_pedido:,.2f}")