#Crie um código em Python que pede qual tabuada o usuário quer ver, em seguida
#imprima essa tabuada. 

n = int(input('Digite qual tabuada você quer ver:'))
for x in range(1,n+1):
    print('='*10)
    print(f'{n} x {x} = {n*x}')