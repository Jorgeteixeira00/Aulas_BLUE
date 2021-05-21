#Faça um programa que leia dez conjuntos de dois valores, o primeiro 
#representando o número do aluno e o segundo representando a 
#sua altura em centímetros.  Encontre o aluno mais alto e o mais baixo. 
#Mostre o número do aluno mais alto e o número do aluno mais baixo, junto com suas alturas.

cont = 0
maiorNum = menorNum = Maior = Menor = 0
while cont <=10:
    print('='*30)
    aluno = int(input('Digite o número do aluno:'))
    altura = float(input('Digite a altura do aluno:'))
    print('='*30)
    cont +=1
    if cont == 1:
        maiorNum = menorNum = aluno
        Maior = Menor = altura
    else:
        if altura > Maior:
            maiorNum = aluno
            Maior = altura 

        if altura < Menor:
            menorNum = aluno
            Menor = altura


print('Aluno mais alto N°:{} Altura:{}'.format(maiorNum, Maior))
print('Aluno mais baixo N°:{} Altura:{}'.format(menorNum, Menor))