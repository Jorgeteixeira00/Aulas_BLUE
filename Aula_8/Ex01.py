# Dada a lista L = [5, 7, 2, 9, 4, 1, 3], escreva um programa que imprima as seguintes informações:
# tamanho da lista.
# maior valor da lista.
# menor valor da lista.
# soma de todos os elementos da lista.
# lista em ordem crescente.
# lista em ordem decrescente.
lista = [5, 7, 2, 9, 4, 1, 3]
print('Tamanho da lista:',len(lista))
print('Maior valor da lista:',max(lista))
print('Menor valor da lista:', min(lista))
print('Soma de todos os valores da lista:', sum(lista))
lista.sort()
print('Ordem crescente:',lista)
lista.reverse()
print('Ordem decrescente:',lista)