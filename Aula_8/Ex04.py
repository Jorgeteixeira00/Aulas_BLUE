#Dada uma string com uma frase informada pelo usuário (incluindo espaços em branco),  conte quantas vezes aparece uma vogal.
# cont = 0
# frase = str(input('Digite uma frase:'))
# for x in range(len(frase)):
#     print(x+1)
#     cont +=1

frase = input("Digite uma frase: ")
vogais = []
cont = 0

for item in frase:
    if item in 'aeiou':
        # num_vogais += 1
        vogais.append(item)
        cont += 1
print(f'Vogais:{vogais}')
print(f'Quantidade:{cont}')