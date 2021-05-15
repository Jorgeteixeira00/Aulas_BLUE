# Um professor, muito legal, fez 3 provas durante um semestre, 
#mas só vai levar em conta as duas notas mais altas para calcular a média.
#Faça uma aplicação que peça o valor das 3 notas, mostre como seria
#a média com essas 3 provas, a média com as 2 notas mais altas,
#bem como sua nota mais alta e sua nota mais baixa.
def prova(a,b,c):
    # n1 = float(input('Digite a primeira nota:'))
    # n2 = float(input('Digite a segunda nota:'))
    # n3 = float(input('Digite a terceira nota:'))

    primeira = n1
    if n2 > n1 and n2 > n3:
        primeira = n2
    elif n3 > n1 and n3 > n2:
        primeira = n3

    segunda = n2
    if n3 < n2 and n3 > n1:
        segunda = n3
    elif n1 < n2 and n1 > n3:
        segunda = n1

    if n1 < n2 and n1 < n3:
        terceira = n1
    elif n2 < n1 and n2 < n3:
        terceira = n2
    else:
        terceira = n3
    
    media3 = (n1+n2+n3)/3

    media_maior = (primeira+segunda)/2
    print('''Média com as 3 notas:{:.2f}
    As notas mais altas foram {} e {}
    A média com essas duas notas foram de:{:.2f}
    A maior nota:{}
    A menor nota:{}'''.format(media3,primeira,segunda,media_maior,primeira,terceira))
    return f'Média com as 3 notas:{media3:.2f}'

n1 = float(input('Digite a primeira nota:'))
n2 = float(input('Digite a segunda nota:'))
n3 = float(input('Digite a terceira nota:'))
print(prova(n1,n2,n3))