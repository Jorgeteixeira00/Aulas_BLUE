# Faça um programa que calcule o salário de um colaborador na empresa XYZ. O salário é pago conforme a quantidade de horas trabalhadas. Quando um funcionário trabalha mais de 40 horas ele recebe um adicional de 1.5 nas horas extras trabalhadas.


def calcular_pagamento(qtd_horas, valor_hora):
    horas = float(qtd_horas)
    taxa = float(valor_hora)
    if horas <=40:
        salario = horas * taxa
    else:
        h_execd = horas - 40
        salario = 40 * taxa +(h_execd*(1.5*taxa))
    return salario

str_horas=input('Digite as horas:')
str_taxa=input('Digite a taxa:')
total_salario = calcular_pagamento(str_horas, str_taxa)
print('O valor se seus rendimentos é R$:',total_salario)