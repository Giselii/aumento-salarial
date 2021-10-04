#Escreve um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
#Para salários superiores a R$ 1250.00, calcule um aumento de 10%.
#Para os inferiores ou iguais, o aumento é de 15 %
salario = float(input('Qual seu salário: '))
if salario > 1250.00:
    print('Voce terá um aumento de 10 %. Seu salário será {}'.format(salario + ((salario * 10) / 100)))
else:
    print('Você terá um aumento de 15 %. Seu salário será {}'.format(salario + (salario * 15) / 100))

