# inputs
nome = input ("Qual o seu nome: ")
idade = int (input("Qual a idade: "))
print ('Nome do jogador:', nome)
print ('Idade do jogador:', idade)

# Condições
if idade > 28:
    print ('Jogador é experiente!')
elif idade > 19 and idade <= 28:
    print ('Jogador jovem.')
else:
    print ('Jogador Novato.')


 # Estrutura de Repetição.
start = 0
stop = 3
lista = ["peixe", "Feijão", "Carne"]

while start < stop:
    print (start)
    start += 1

# Adicionado elementos em uma lista com estrutura de repetição
start= 0
while start < stop:
    produto = input('Adicione um produto: ')
    lista.append(produto)
    print (start)
    start += 1
    print (lista)
    

