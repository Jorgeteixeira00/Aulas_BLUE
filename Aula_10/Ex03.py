# Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. 
# Os códigos utilizados são:
# 1 , 2, 3  - Votos para os respectivos candidatos (você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
# 5 - Voto Nulo
# 6 - Voto em Branco
# Faça um programa que calcule e mostre:
# O total de votos para cada candidato;
# O total de votos nulos;
# O total de votos em branco;
# A percentagem de votos nulos sobre o total de votos;
# A percentagem de votos em branco sobre o total de votos. Para finalizar o conjunto de votos tem-se o valor zero.


def urna():
    print('='*30)
    print('{:^30}'.format('ELEIÇOES 2021'))
    print('='*30)

def final():
    print('='*30)
    print('{:^30}'.format('TOTAL DE VOTOS'))
    print('='*30)

def linha():
    return print('='*20)

Bolsonaro = []
Lula = []
LucianoHulk = []
Ciro = []
Nulo = []
Branco = []

urna()
while True:
    print('''
    [1] Bolsonaro
    [2] Lula
    [3] Luciano Hulk
    [4] Ciro
    [5] Nulo
    [6] Branco
    ''')
    opcao = int(input('Digite seu voto:'))
    if opcao == 0: break
    else:
        if opcao == 1:
            Bolsonaro.append(opcao)
        elif opcao == 2:
            Lula.append(opcao)
        elif opcao == 3:
            LucianoHulk.append(opcao)
        elif opcao == 4:
            Ciro.append(opcao)
        elif opcao == 5:
            Nulo.append(opcao)
        else:
            Branco.append(opcao)

votos_bolsonaro = len(Bolsonaro)
votos_lula = len(Lula)
votos_luciano = len(LucianoHulk)
votos_ciro = len(Ciro)
votos_nulos = len(Nulo)
votos_brancos = len(Branco)
total_votos = (votos_bolsonaro+votos_lula+votos_luciano+votos_ciro+votos_nulos+votos_brancos)
percentual_nulos = (votos_nulos / total_votos) * 100
percentual_brancos = (votos_brancos / total_votos) * 100

final()
print(f'''
==================================
BOLSONARO:{votos_bolsonaro} votos
==================================
LULA:{votos_lula} votos
==================================
LUCIANO HULK:{votos_luciano} votos
==================================
CIRO:{votos_ciro} votos
==================================
NULOS:{votos_nulos} votos
==================================
BRANCOS:{votos_brancos} votos
==================================
PERCENTUAL DE VOTOS NULOS:{percentual_nulos}%
==================================
PERCENTUAL DE VOTOS BRANCOS:{percentual_brancos}%
''')