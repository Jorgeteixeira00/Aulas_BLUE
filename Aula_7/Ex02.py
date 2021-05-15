#Escreva uma função que recebe dois números (a e b)como parâmetro e retorna True caso a soma dos dois seja maior que um terceiro parâmetro, chamado limite.
def maior_soma(a,b,l):
    if n1 + n2 > limite:
        print('A soma entre {} e {} é maior que o limite!'.format(n1,n2))
    else:
        print('A soma entre {} e {} não é maior que o limite!'.format(n1,n2))
n1 = int(input('Digite o primeiro número:'))
n2 = int(input('Digite o segundo número:'))
limite = int(input('Digite o limite:'))
maior_soma(n1, n2, limite)