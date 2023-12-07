# Iniciando python
# Fazendo o primeiro print
print ("Olá mundo.")

# Variaveis
# Declarações
nome = "Riquelme" # String
idade = 15 # Numbers
print (f"Meu nome é: {nome}\nMinha idade é: {idade}")

# booleans:
# false - falso, true - Verdadeiro
print (idade < 18)

# Lista 
lista_de_compras = ["Arroz", "Feijão", "2kg de carne", "Macarrão"]
lista_de_compras.append ("farinha")
print(lista_de_compras)
lista_de_compras.remove ("Arroz")
print (lista_de_compras)

# Objetos:
objeto = {
    'nome' : 'Lionel Messi',
    'idade' : 35,
    'gols' : 800,
}
print (objeto ["gols"])
