#(DESAFIO) Escreva um programa que determine todos os números de 4 algarismos que possam ser separados em dois números de dois algarismos que somados e elevando-se a soma ao quadrado obtenha-se o próprio número.

# Exemplo: 3025 = 55 e 55**2 é igual á 3025

for c in range(1000,10000):
    p1 = c // 100
    p2 = c % 100
    if (p1+p2)**2 == c:
        print(c)
