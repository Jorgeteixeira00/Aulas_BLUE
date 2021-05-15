#Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma desses três argumentos. 

def soma(a, b, c):
    soma = a + b + c
    return soma
a = int(input('Digite o 1° número:'))
b = int(input('Digite o 2° número:'))
c = int(input('Digite o 3° número:'))
print('A soma entre esse números é:',soma(a, b, c))