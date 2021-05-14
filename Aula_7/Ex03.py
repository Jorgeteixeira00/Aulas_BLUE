#Crie uma função que receba uma string como argumento e retorne a mesma string em letras maiúsculas. Faça uma chamada à função, passando como parâmetro uma string
def maiúsculas(string):
    return string.upper()

string = str(input('Digite uma frase:'))
print(maiúsculas(string))