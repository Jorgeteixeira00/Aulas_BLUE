#Escreva uma função que recebe dois parâmetros e imprime o menor dos dois.Se eles forem iguais, imprima que eles são iguais.
def menor(n1,n2):
    if a < b:
        print('{} é o menor!'.format(a))
    elif b < a:
        print('{} é o menor!'.format(b))
    else:
        print('SÃO IGUAIS!')
a = int(input('Digite o primeiro número:'))
b = int(input('Digite o segundo número:'))
menor(a, b)