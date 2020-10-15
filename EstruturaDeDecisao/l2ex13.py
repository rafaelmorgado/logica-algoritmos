''' 13) Faça um Programa que leia um número e exiba o dia correspondente da semana. (1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido. '''

def switch(opcao):
    dias = {
        1: "1-Domingo",
        2: "2-Segunda-feira",
        3: "3-Terça-feira",
        4: "4-Quarta-feira",
        5: "5-Quinta-feira",
        6: "6-Sexta-feira",
        7: "7-Sábado"
    }
    return dias.get(opcao, "Opção inválida.")

opcao = int(input("Informe o dia da semana: "))
print (switch(opcao))