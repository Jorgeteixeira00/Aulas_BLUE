#Escreva um programa onde o usuário digita uma frase e essa frase retorna sem nenhuma vogal.

frase = input("Digite uma frase: ")
consoantes = []
cont = 0

for item in frase:
    if item not in 'aeiou':
        consoantes.append(item)
        cont += 1
print(f'Consoantes:{consoantes}')
print(f'Quantidade:{cont}')