sal1 = float(input('Digite seu salario: R$ '))
print(sal1)
sal2 = sal1 + (sal1 * 15 / 100)
print('Com o aumento de 15%, seu salario de R${:.2f}, passou a ser de R${:.2f} '.format(sal1, sal2))
