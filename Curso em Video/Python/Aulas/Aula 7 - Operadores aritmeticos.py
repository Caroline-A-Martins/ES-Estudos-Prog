n1 = int(input('Digite um valor: '))
print(n1)
n2 = int(input('Digite outro valor: '))
print(n2)
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
p = n1 ** n2
di = n1 // n2
print('A soma é {}, a subtração é {}, a multiplicação é {}, a divição é {} '.format(a, s, m, d), end='  ')
print('A divição inteira é {} e a potencia é {}'.format(di, p))
