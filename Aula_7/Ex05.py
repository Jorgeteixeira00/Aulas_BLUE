#Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros: o nome de um jogador e quantos gols ele marcou.
#O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
def ficha(nome,gols):
    return f'Nome:{nome}\nGols:{gols}'
nome = str(input('Digite o nome do Jogador:'))
gol = int(input('Digite os gols:'))
print(ficha(nome, gol))