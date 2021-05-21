# Exercício 1 - Escreva um programa que pede a senha ao usuário, e só sai do looping quando digitarem corretamente a senha.
senha = '123456' 
entrada = input('Digite a senha:').strip()
while entrada != senha:
    print('Senha incorreta!')
    entrada = input('Digite a senha novamente:')
print('Acesso liberado!')