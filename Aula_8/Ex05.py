#Desenvolva um código que pergunte um número n para o usuário  e exiba todos seus divisores. Caso seja um número primo, o programa ainda deve informar que se trata de um número primo! 
cont = 0
n = int(input('Digite um número:'))
for x in range(1,n+1):
    if n % x == 0:
        print('{} é divisivel por:{}'.format(n, n/x))
        cont += 1
if cont == 2:
    print('É um número primo!')
else:
    print('Não é um número primo!')