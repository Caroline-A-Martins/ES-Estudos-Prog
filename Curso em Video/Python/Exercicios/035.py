# Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou
# não formar um triângulo.
print('-=-'*10)
print('Analisador de triangulos')
print('-=-'* 10)
r1 = float(input('Primeiro segmento: '))
print(r1)
r2 = float(input('Segundo segmento: '))
print(r2)
r3 = float(input('Terceiro segmento: '))
print(r3)
if r1 < r2 + r3 and r2 < r1 + r3 or r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO.')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO.')
