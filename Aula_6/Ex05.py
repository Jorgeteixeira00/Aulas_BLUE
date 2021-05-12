#Faça um programa que calcule através de uma função o IMC de uma pessoa que tenha 1,68 e pese 75kg.
'''def IMC(m=75,a=1.68):
    return m / a ** 2
print(IMC())'''

#PARTE 2 onde o usuario insere os valores
def IMC(m,a):
    return m / a **2
massa = float(input('Digite a sua massa:'))
altura = float(input('Digite a sua altura:'))
print('Seu IMC é:',IMC(massa,altura))