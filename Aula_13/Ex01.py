# Crie um programa onde você cadastre a data de nascimento (dd/mm/aa) de algumas
# celebridades em um dicionário. Ao escolher uma celebridade, seu programa deve
# retornar a data completa. Não esqueça de validar se a celebridade escolhida está
# presente em seu dicionário. 

celebridades = {'Abraham Lincoln':'12 de fevereiro de 1809','Benjamin Franklin':'17 de janeiro de 1706','Albert Einstein':'4 de Janeiro de 1879','Isaac Newton':'4 de janeiro de 1643','Nikola Tesla' : '10 de julho de 1856'
}

for itens in celebridades:
    print(itens)

nome = input('De quem você queria saber a data de nascimento:').title()
print(celebridades.get(nome,f'Desculpe, o nome {nome} não foi encontrado.'))
