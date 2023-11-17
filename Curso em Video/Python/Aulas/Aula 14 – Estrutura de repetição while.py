for c in range(1, 3):
    print(c)
print('fim')

c = 1  # C é igual a 1
while c < 10:  # Enquanto c for menor que 10
    print(c)
    c = c + 1  # isso pq quando o laço vai se repetir, o c adiciona 1
print('FIM')

for c in range(1, 3):  # Aqui eu sei q o programa vai me fazer a mesma pergunta 3 vezes
    print(c)
print('fim')

# neste caso eu n sei o limite, o que eu sei é q, se o usuario digitar 0 o programa para de funcionar e pula direto pro "print('fim'),
# por isso o programa pode funcionar infinitamente enquanto n for digitado o número 0
n = 1
while n != 0:
    n = int(input('Digite o valor: '))
    print(n)
print('fim')

r = 'S'
while r == 'S':
    n = int(input('Digite o valor: '))
    print(n)
    r = str(input('Quer continuar? [S/N]')).upper()
    print(r)
print('fim')

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite o valor: '))
    print(n)
    if n != 0:
        if n % 2 == 0:
            par += 1  # a quantidade de pares recebe mais um
        else:
            impar += 1  # a quantidade de impares recebe mais um
print('Você digitou {} valores pares e {} valores impares'.format(par, impar))

