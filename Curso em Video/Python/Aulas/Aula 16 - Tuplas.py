# Tuplas são imutaveis, ou seja, elas não mudam
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

print('print(lanche)')
print(lanche)
print('print(lanche[1])')
print(lanche[1])  # n esquecer do indice

print('print(lanche[3])')
print(lanche[3])

print('print(lanche[-2])')
print(lanche[-2])  # o pudim é o menos 1, então o menos 2 é a pizza

print('print(lanche[1:3])')
print(lanche[1:3])  # vai contar a partir so indice 1 e ignorar o indice 3

print('print(lanche[2:])')
print(lanche[2:])  # do indice 2 até o final

print('print(lanche[:2])')
print(lanche[:2])  # do início até o indice 2, lembrando, ignorando o indice 2

print('print(lanche[-3:])')
print(lanche[-3:])

print(sorted(lanche))  # Organizar sua tupla

for comida in lanche:
    print(f'Eu vou comer {comida}')
print()

for cont in range(0, len(lanche)):
    print(f'O {lanche[cont]} está na posição {cont}')
print()

for posi, comida in enumerate(lanche):
    print(f'{comida} está na posição {posi}')
print()

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5))  # quantas vezes aparece o número 5

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c)
print(f'O 8 está na posição {c.index(8)}')  # index mostra a posição do elemento pelo indice dele
