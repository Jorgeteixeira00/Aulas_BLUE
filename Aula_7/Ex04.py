#Crie um programa que tenha uma função chamada voto () que vai receber como  parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições. Para resolver esse exercício, pesquise sobre a função date da biblioteca Datetime.
def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade <16:
        return f'Com {idade} anos VOTO:NEGADO'
    elif idade >=16 and idade <18:
        return f'Com {idade} anos VOTO:OPCIONAL'
    else:
        return f'Com {idade} anos VOTO:OBRIGATORIO'

nasc = int(input('Em que ano você nasceu:'))
print(voto(nasc))