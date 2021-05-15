# Faça um jogo da forca. O programa terá uma lista de palavras lidas de
# um arquivo texto e escolherá uma aleatoriamente. O jogador poderá
# errar 6 vezes antes de ser enforcado. 

import random
lista = input('Digite uma lista de palavras separadas por espaço:')
lista = (lista.strip()).split(' ')

#indice = random.randrange(0,len(lista))
#palavra = lista[indice]
if len(lista) == 1:
    palavra = lista[0].upper()
else:
    palavra = random.choice(lista).upper()

palavra_forca = ['_' for i in palavra]
# palavra_forca = ['_','_','_','_','_','_','_']
# " ".join(palavra_forca) =>  _ _ _ _ _ _ _
chance = 0

print('A palavra é: ',end=' ')
print('     '.join(palavra_forca))

maximo = len(palavra) + 6 # comprimento da palavra + 6 chances para errar
# for i in range(13):

for i in range(maximo):
    # verificar condições de parada: GANHOU ou PERDEU
    if palavra_forca.count('_') == 0 or chance == 6: break
    letra = input('Digite uma letra: ').upper()
    if letra in palavra_forca:
        print('Você já digitou esta letra antes. A palavra é: ', end=' ')
        print(' '.join(palavra_forca))
        continue
    if letra in palavra:
        print('A palavra é:', end=' ')
        for n in range(len(palavra)):
            if letra == palavra[n]:
                del palavra_forca[n]
                palavra_forca.insert(n, letra)
                 # palavra_forca[n] = letra
        print(' '.join(palavra_forca))
    else:
        chance += 1
        if chance != 6:
            print('Você errou pela' + str(chance) + ' vez.Tente novamente!')

if palavra_forca.count('_') == 0:
    print('Parabéns! Você acertou a palavra!')
else:
    print('Você errou pela 6° vez\nFORCA! VOCÊ PERDEU')