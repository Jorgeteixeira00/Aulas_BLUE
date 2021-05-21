# 2. Crie um programa que gerencie o aproveitamento de um jogador de futebol. O
# programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a
# quantidade de gols feito em cada partida. No final tudo isso será guardado em um
# dicionário, incluindo o total de gols feitos durante o campeonato.

jogador = {}
gol_por_partidas = []
jogador['nome'] = input('Digite o nome do jogador:')
total = int(input('Digite o total de partidas jogadas:'))

for i in range(total):
    gol_por_partidas.append(int(input(f'Quantidade de gols na partida {i + 1}:')))

jogador['gols'] = gol_por_partidas[:]
jogador['total'] = sum(gol_por_partidas)

print('='*35)
print('Nome do jogador:',jogador['nome'])
print('='*35)
print(f"O jogador {jogador['nome']} jogou {len(jogador['gols'])} partidas")
print('='*35)

for k,v in enumerate(jogador['gols']):
    print(f' - Na partida {k}, ele fez {v} gols.')
print('='*35)
print(f"O jogador {jogador['nome']} fez um total de {jogador['total']} gols no campeonato")