from random import randint

"""num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort()
num.insert(2, 2)
if 4 in num:
    num.remove(4)
else:
    print(f'Não achei o número 4')
print(num)
print(f'Essa lista em {len(num)} elementos.')"""
valores2 = []
valores = list()
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f'{v}...', end='')
print()
for c, v in enumerate(valores):
    print(f'Na posição {c + 1} encontrei o valor: {v}')
print('Final da lista')
print()

a = [2, 3, 4, 7]
b = a
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print()

a = [2, 3, 4, 7]  # Cria uma ligação entre as listas, ou seja, se uma mudar as duas mudam
b = a
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')
print()

a = [2, 3, 4, 7]  # Cria uma cópia de uma lista, ou seja, se a lista b mudar a lista a se mantem da mesma forma
b = a[:]
b[2] = 8
print(f'Lista A: {a}')
print(f'Lista B: {b}')

