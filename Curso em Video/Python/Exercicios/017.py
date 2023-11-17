from math import hypot
co = float(input('Comprimento do cateto oposto: '))
print(co)
ca = float(input('Comprimento do cateto adjacente: '))
print(ca)
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))

'''hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hi))'''
