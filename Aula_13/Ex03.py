# 3. Crie um programa, utilizando dicionário, que simule a baixa de estoque das vendas
# de um supermercado. Não esqueça de fazer as seguintes validações:
#       estoque = {"tomate": [1000, 2.30], "alface": [500, 0.45], "batata": [2001, 1.20],
#       "feijão": [100, 1.50]}
#   Produto Indisponível
#   Produto Inválido
#   Quantidade solicitada não disponível
# O programa deverá mostrar para o cliente a quantidade de itens comprados e o total a pagar.
estoque_fixo = {"tomate": 1000, "alface": 500, "batata": 2001, "feijão": 100}
estoque = {"tomate": [1000, 2.30], "alface": [500, 0.45], "batata": [2001, 1.20], "feijão": [100, 1.50]}
total = 0
 
print("*-=-*"*10)
print("SUPERMERCADO T2B")
print("*-=-*"*10)
#produto = input("Digite o nome do produto ou 0 para sair: ")
#while produto != '0':
#    qtd = int(input(f"Digite a qtd do produto \"{produto}\": "))
#    valor = float(input(f"Digite o valor unitário do produto \"{produto}\": "))
 
while True:
    prod = input("Digite um produto para ser adquirido ou FIM para sair: ")
    if prod == "FIM": break
    if prod in estoque:
        qtd = int(input("\tDigite a quantidade deste produto: "))
        if qtd < estoque[prod][0]:
            preco_unit = estoque[prod][1]
            custo = qtd*preco_unit
            print(f"\t{prod}:\t{qtd}\tx\t{preco_unit:3.2f}\t=\t{custo:4.2f}")
            estoque[prod][0] -= qtd
            total += custo
        elif estoque[prod][0] == 0:
            print("Produto indisponível!")
        else:
            print("Quantidade não disponível!")
    else:
        print("Produto inválido!")
 
print("")
print("*-=-*"*10)
print("COMPRA REALIZADA")
print("*-=-*"*10)
for k,v in estoque.items():
    if v[0] != estoque_fixo[k]:
        qtd = estoque_fixo[k] - v[0]
        custo = qtd*v[1]
        print(f"{k}:\t\t{qtd}\tx\tR$ {v[1]:6.2f}\t=\tR$ {custo:4.2f}")
print("*-=-*"*10)
print(f"Valor total da compra: R$ {total:6.2f}")

