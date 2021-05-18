# O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a
# metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi
# contratado para desenvolver o programa que monta a tabela de preços de pães, de 1
# até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo
# abaixo:

preço = float(input('Digite o preço do pão R$:'))
print('Preço do pão:{:.2f}'.format(preço))
print('Panificadora de Pão - Tabela de preço')
for x in range(1,51):
    print('{} - R${:.2f}'.format(x, preço*x))