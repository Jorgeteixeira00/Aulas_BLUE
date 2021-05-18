#O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
#  Faça um programa que implemente uma caixa registradora rudimentar. O programa deverá receber um número desconhecido
#  de valores referentes aos preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final
#  da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu, para
#  então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial, para registrar
#  a próxima compra. A saída deve ser conforme o exemplo abaixo:
from time import sleep

print('='*30)
print('LOJAS TABAJARA')
print('='*30)
listaProdutos = []
numero_de_produtos = 1

while True:
    valor = float(input(f'Digite o valor do produto {numero_de_produtos}:'))
    print('='*30)
    numero_de_produtos += 1
    listaProdutos.append(valor)
    if valor == 0: break

Total = sum(listaProdutos)
print(f'TOTAL R$:{Total:.2f} reais')
dinheiro = float(input('Digite o quanto você irá pagar:'))
troco = dinheiro - Total

print('IMPRIMINDO NOTINHA FISCAL')
sleep(2)

print(f'''
NOTINHA FISCAL
Total de produtos:{numero_de_produtos}
Valor total R$:{Total:.2f} reais
Dinheiro R$:{dinheiro:.2f} reais
Troco R$:{troco:.2f} reias
''')