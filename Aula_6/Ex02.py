#Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de caractere ‘P’, se seu argumento for positivo, ‘N’, se seu argumento for negativo e ‘0’ se for 0.
def pn(n):
    if n > 0:
        print('POSITIVO')
    elif n < 0:
        print('NEGATIVO')
    else:
        print('NEUTRO')
n = int(input('Digite um número:'))
print('Este número é:',end='')
pn(n)