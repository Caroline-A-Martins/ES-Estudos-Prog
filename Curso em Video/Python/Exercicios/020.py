from random import shuffle
n1 = str(input('Primeiro aluno: '))
print(n1)
n2 = str(input('Segundo aluno: '))
print(n2)
n3 = str(input('Terceiro aluno:'))
print(n3)
n4 = str(input('Quarto aluno:'))
print(n4)
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será:')
print(lista)
