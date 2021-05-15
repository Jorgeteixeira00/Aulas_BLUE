#Escreva uma função que, dado um número nota representando a nota de um estudante,  converte o valor de nota para um conceito (A, B, C, D, E e F).
def classificacao(valor):
    if valor >=9:
        print('NOTA:A')
    elif valor >=8:
        print('NOTA:B')
    elif valor >=7:
        print('NOTA:C')
    elif valor >=6:
        print('NOTA:D')
    else:
        print('NOTA:F')
valor = float(input('Digite o valor:'))
classificacao(valor)