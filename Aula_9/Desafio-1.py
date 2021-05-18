#(DESAFIO) Desenvolva um código em Python que gere um número aleatório de 1 a 100 e dê ao usuário 10 chances para acertá-lo. A cada tentativa, deve ser impressa a quantidade de tentativas restantes e se o número aleatório é maior ou menor do que o número inserido na tentativa atual. Se o usuário não acertar em 10 tentativas, informe qual o número aleatório. [Dica: use a função randint para gerar o número aleatório]

from random import randint
aleatorio = randint(1,100)
tentativas = 10

while True:
    print('='*20)
    numero = int(input('\033[33mDigite um número:'))
    print('='*20)
    tentativas -= 1
    if numero == aleatorio:
        print('\033[32mPárabens, você acertou!')
        break
    elif tentativas < 1:
        print('\033[31mPoxa, Você perdeu!')
        break
    else:
        if numero < aleatorio:
            print('\033[33mUM POUCO MAIS')
        else:
            print('\033[33mUM POUCO MENOS')
    print(f'\033[33mFaltam {tentativas} tentativas!')