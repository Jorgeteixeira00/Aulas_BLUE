#Faça um script que peça ao usuário o número de matérias da escola, ou seja,
#um inteiro positivo. Em seguida, ele vai digitando o valor de cada nota, 
#de cada matéria e isso será armazenado numa lista. Ao final, seu script 
#deverá fornecer a média geral do aluno.

materias = int(input('Digite o número de máterias:'))
listaMedia = []

for c in range(1, materias + 1):
    nota = int(input(f'Nota da matéria {c}:'))
    listaMedia.append(nota)

somaMedia = sum(listaMedia)
media = somaMedia / materias
print(f'A média total das notas é:{media:.2f}')
