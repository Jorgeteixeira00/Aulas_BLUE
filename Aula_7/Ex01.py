#Escreva uma função que recebe dois parâmetros (números) e imprime o menor dos dois. Se eles forem iguais,imprima que são valores idênticos.
def menor(v1,v2):
    if n1 < n2:
        print('{} é o menor!'.format(n1))
    elif n2 < n2:
        print('{} é o menor!'.format(n2))
    else:
        print('São iguais!')
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
menor(n1,n2)