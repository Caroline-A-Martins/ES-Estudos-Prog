# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final,
# mostre os 10 primeiros termos dessa progressão.

print('=' * 20)
print('10 TERMOS DE UMA PA')
print('=' * 20)

p = (int(input('Primeiro termo: ')))
print(p)
r = (int(input('Razão')))
print(r)
d = p + (10-1) * r
for c in range(p, d + r, r):
    print('{}'.format(c), end=' - ')
print('ACABOU \n')
