#Codifique um jogo da FORCA. A pessoa digita uma palavra e tem que acertar a palavra digitada.

import random

lista = input('Digite um lista de separadas por espaço: ')
lista = (lista.strip()).strip(' ')

if len(lista) == 1:
    palavra = lista[0].upper()
else:
    palavra = random.choice(lista).upper()

palavra_forca = ['_' for i in palavra]
chance = 0

print('A palavra é: ', end=' ')
print(' '.join(palavra_forca))

while palavra_forca.count('_') != 0 and chance != 6:
    letra = input('Digite uma letra: ').upper()
    if letra in palavra_forca:
        print('Você já digitou esta letra antes. A palavr é: ', end=' ')
        print(' '.join(palavra_forca))
        continue
    if letra in palavra:
        print('A palavra é: ', end=' ')
        for n in range(len(palavra)):
            if letra == palavra[n]:
                del palavra_forca[n]
                palavra_forca.insert(n, letra)
        print(' '.join(palavra_forca))
    else:
        chance += 1
        if chance != 6:
            print('Você errou pela ' + str(chance) + 'a vez. Tente novamente')

if palavra_forca.count('_') == 0:
    print('Parabéns! Você acertou a palavra!')
else:
    print('Você errou pela 6a vez.\nFORCA! VOCÊ PERDEU')