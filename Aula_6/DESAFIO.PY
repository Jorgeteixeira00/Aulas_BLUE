# DESAFIO -  Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data e retorne NULL caso a data seja inválida. Considere que Fevereiro tem 28 dias e que a cada 4 anos temos ano bisexto, sendo que nesses casos Fevereiro terá 29 dias.

def dataImpressa(data):  
    dia = int(data[:2])
    mes = data[3:5]
    ano = int(data[6:])
    if mes > "12" or mes == "00":
        print("Data Inválida!")
    if mes == "01":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Janeiro de {ano}.")
    elif mes == "03":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Março de {ano}.")
    elif mes == "05":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Maio de {ano}.")
    elif mes == "07":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Julho de {ano}.")
    elif mes == "08":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Agosto de {ano}.")
    elif mes == "10":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Outubro de {ano}.")
    elif mes == "12":
        if dia > 31:
            print ("Data Inválida!")
        else:
            print (f"{dia} de Dezembro de {ano}.")
    elif mes == "04":
        if dia > 30:
                print("Data Inválida!")
        else:
            print (f"{dia} de Abril de {ano}.")
    elif mes == "06":
        if dia > 30:
            print("Data Inválida!")
        else:
            print (f"{dia} de Junho de {ano}.")
    elif mes == "09":
        if dia > 30:
            print("Data Inválida!")
        else:
            print (f"{dia} de Setembro de {ano}.")
    elif mes == "11":
        if dia > 30:
            print("Data Inválida!")
        else:
            print (f"{dia} de Novembro de {ano}.")

    elif mes == "02": 
        if (ano % 4 == 0 or ano % 100 != 0) or ano % 400 == 0:
            if dia > 29:
                print("Data Inválida!")
            else:
                print (f"{dia} de Fevereiro de {ano}.")
        if (ano % 4 != 0 or ano % 100 == 0) or ano % 400 != 0:
            if dia > 28:
                print("Data Inválida!")
            else:
                print (f"{dia} de Fevereiro de {ano}.")
            
  
data = input("Digite uma data (Formato DD/MM/AAA): ")

dataImpressa(data)