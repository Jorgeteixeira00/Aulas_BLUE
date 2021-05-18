#Crie um código em Python para exibir a contagem de dígitos de um número inteiro positivo informado pelo usuário
num = int(input('Digite um número:'))
for x in range(1,num + 1):
    print(f'{x}', end=' ')