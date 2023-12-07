print("Bem vindo a lanchonete")
print(
    """Cardápio
    | Código | Descrição | Valor|
    | 100    | X-tudo    | 15,00|
    | 101    | X-egg     | 12,00|
    | 102    | X-salada  | 10,00|
    | 103    | X-bacon   | 10,00|
    | 200    | Coca-cola | 15,00|
    | 201    | Bacana    | 03,50|
    | 202    | Guaraná   | 10,00|
    | 203    | Fanta     | 09,00|
"""
)

start = 0
valor_total = 0

while start == 0:
    codigo = input ("Entre com o código desejando: ")
    if codigo =="100":
        print ('Você escolheu um x-tudo no valor de 15 reais')
        valor_total += 15.0
    elif codigo == "101" :
        print ('Você escolheu um X-egg no valor de 12 reais')
        valor_total += 12.0
    elif codigo == "102" :
        print ('Você escolheu um X-salada no valor de 10 reais')
        valor_total += 10.0
    elif codigo == "103" :
        print ('Você escolheu um X-bacon no valor de 10 reais')
        valor_total += 10.0
    elif codigo == "200" :
        print ('Você escolheu uma Coca-Cola no valor de 15 reais')
        valor_total += 15.0
    elif codigo == "201" :
        print ('Você escolheu um Bacana por 3 reais e 50 centavos')
        valor_total += 3.5
    elif codigo == "202" :
        print ('Você escolheu um Guaraná por 10 reais')
        valor_total += 10.0
    elif codigo == "203" :
        print ('Você escolheu uma Fanta por 9 reais')
        valor_total += 9.0
    else:
        print ("Codigo invalido")
    resposta = input ("\nDeseja fazer mais algum pedido? 1-Sim, 2-Não\n Resposta: ")
    if resposta == "1":
        continue
    else:
        print("Valor do seu pedido é:", valor_total )
        break