#  Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120
"""from math import factorial
n = int(input('Digite um número para ser fatorado: '))
print(n)
f = factorial(n)
print('O fatorial de {} é {}'.format(n, f))"""

n = int(input('Digite um número para calcular seu fatorial: '))
print(n)
f = 1  # parafazer uma soma limpa começamos com 0, mas para uma multiplicação começamos com 1, pois um num x 0 = 0
c = n  # o contador recebe n
print('Calculando {}: '.format(n), end='')
while c > 0:  # enquanto o contador for maior q 0
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')  # se o c for maior q 1 senão mostre um =
    f = f * c
    c = c - 1
print('{}'.format(f))
