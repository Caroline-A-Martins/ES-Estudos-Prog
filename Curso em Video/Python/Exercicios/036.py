# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o
# valor da casa, o salário do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do
# salário ou então o empréstimo será negado.
casa = float(input('Valor da casa: R$'))
print(casa)
salario = float(input('Salário do comprador: R$ '))
print(salario)
anos = float(input('Quantos anos de financiamento? '))
print(anos)
pres = casa / (anos*12)
mini = salario * 30/100
print('Para pagar uma casa de R${:.2f} em {:.2f} anos, a prestação será de R${:.2f} '.format(casa, anos, pres))
if pres <= mini:
    print('Emprestimo CONCEDIDO!')
else:
    print('Emprestimo NEGADO!')
