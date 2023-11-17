# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado.
# No final, mostre a matriz na tela, com a formatação correta.
from random import randint
matriz = []
for li in range(0, 3):
    linha = []
    for c in range(0,3):
        linha.append(randint(0, 500))
    matriz.append(linha)
print('-='*30)
for li in range(3):
    for c in range(3):
        print(f'[{matriz[li][c]:^5}]', end='')
    print()