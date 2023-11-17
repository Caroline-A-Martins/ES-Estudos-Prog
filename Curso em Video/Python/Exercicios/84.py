# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai += 1
        if temp[1] < men:
            men += 1
    princ.append(temp[:])
    temp.clear()
    r = str(input('Deseja continuar? [S/N]'))
    if r in 'Nn':
        break

print(f'Ao todo foram {len(princ)} pessoas cadastradas')
print(f'O maior peso foi de {mai}Kg. Peso de', end='')
for pes in princ:
    if pes[1] == mai:
        print(f'[{pes[0]}] ', end='')
print()
print(f'O menor peso foi de {men}Kg. Peso de ', end='')
for pes in princ:
    if pes[1] == men:
        print(f'[{pes[0]}] ', end='')
print()

