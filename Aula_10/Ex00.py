# Crie um laço while que vai pedir para o usuário dois números e faça a soma dos dois. Enquanto a soma não for 50, ele deve continuar repetindo.
n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
soma = n1+n2 
while soma != 50:
    print('III AINDA NÃO!')
    n1 = int(input('Digite novamente outro número:'))
    n2 = int(input('Digite novamente outro número:'))
    soma = n1+n2
print('Ai sim em, conseguiu!')