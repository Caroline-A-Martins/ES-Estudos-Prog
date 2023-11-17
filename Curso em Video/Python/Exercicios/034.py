# Exercício Python 34: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Digite seu salario: '))
print(salario)
if salario <= 1250.0:
    aumento = salario * (15 / 100)
else:
    aumento = salario * (10 / 100)
total = salario + aumento
print('Seu salario de R${:.2f} teve um aumento de R${:.2f} com isso você recebera R${:.2f}'.format(salario, aumento, total))



