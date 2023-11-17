print('Desafio 01')

n1 = int(input('Digite um numero:'))
n2 = int(input('Digite outro numero:'))
s = n1 + n2
# print('O valor de', n1, 'e', n2, "é igual a", s)
print('A soma entre {} e {} vale {}'.format(n1, n2, s))

print('Desafio 02')

a = input(print('Digite algo:'))
print("O tipo primitivo desse valor é:", type(a))
print('Tem espaços?', a.isupper())
print('É um numero?', a.isnumeric())
print('É alfabetico?', a.isalpha())
print('É alfanumerico?', a.isalnum())
print('Está em maiusculas?', a.isupper())
print('Está em minusculo?', a.islower())

