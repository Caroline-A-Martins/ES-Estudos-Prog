# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 10000000
for p in range(1, 6):
    peso = float(input('Peso da {}º pessoa \n'.format(p)))
    print(peso)
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi {}Kg'.format(maior))
print('O menor pedo lido foi {}Kg'.format(menor))
