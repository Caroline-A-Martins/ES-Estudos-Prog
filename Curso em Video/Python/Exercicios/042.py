# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

print('-=-' * 10)
print('Analisador de triangulos')
print('-=-' * 10)
r1 = float(input('Primeiro segmento: '))
print(r1)
r2 = float(input('Segundo segmento: '))
print(r2)
r3 = float(input('Terceiro segmento: '))
print(r3)
if r1 < r2 + r3 and r2 < r1 + r3 or r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR UM TRIANGULO', end="")
    if r1 == r2 == r3:
        print(' EQUILÁTERO')
    elif r1 != r2 != r3 != r1:
        print(' ESCALENO')
    else:
        print(' ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR UM TRIANGULO ')
