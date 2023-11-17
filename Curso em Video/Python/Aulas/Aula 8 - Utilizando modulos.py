import math

num = int(input('Digite um numero: '))
print(num)
raiz = math.sqrt(num)
print('A raiz de {} é igual a {:.2f}'.format(num, raiz))

# Outra maneira de fazer que tb dá certo
# from math import sqrt
# num = int(input('Digite um numero: '))
# print(num)
# raiz = sqrt(num)
# print('A raiz de {} é igual a {:.2f}'.format(num, raiz))
