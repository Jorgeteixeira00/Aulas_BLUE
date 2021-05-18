# Crie um código em Python que receba uma lista de nomes informados pelo usuário
# com tamanho indefinido (a lista deve ser encerrada quando o usuário digitar 0) e, na
# sequência, receba um nome para que seja verificado se este consta na lista ou não.
# Observação: ignorar diferenças entre maiúsculas e minúsculas.

listaNomes = []

for c in range(1000):
    nome = str(input('Adicione um nome a lista:')).upper()
    if nome == '0':
        break
    else:
        listaNomes.append(nome)
    print(listaNomes)

buscar = str(input('Busque um nome na lista:')).upper()
if buscar in listaNomes:
    print(f'{buscar} está na lista!')
else:
    print(f'{buscar} não está na lista!')