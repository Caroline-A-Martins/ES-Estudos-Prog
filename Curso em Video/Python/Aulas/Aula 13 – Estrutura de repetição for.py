for c in range(0, 6):
    print(c)
print('-='*5)
for c in range(0, 6):
    print('Oi')
print('-='*5)
for c in range(6, 0, -1):
    print(c)
print('-='*5)
for c in range(0, 7, 2):
    print(c)
print('-='*5)
print('Tchau')
print('-='*5)

n = int(input('Digite um numero: '))
print(n)
for c in range(0, n+1):
    print(c)
print('FIM')

i = int(input('Inicío: '))  # inicio da contagem
print(i)
f = int(input('Fim: '))  # fim da contagem
print(f)
p = int(input('Passo: '))  # em quantos será contado ex: 2 em 2
print(p)
for c in range(i, f + 1, p):
    print(c)
print('FIM')

for c in range(0, 3):
    n = int(input('Digite um valor: '))
    print(n)
print('FIM')

s = 0
for c in range(0, 3):
    n = int(input('Digite um valor: '))
    print(n)
    s = s+n
print('A somatoria desses valores foi {}'.format(s))
