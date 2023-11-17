from random import choice
n1 = str(input('Primeiro aluno: '))
print(n1)
n2 = str(input('Segundo aluno: '))
print(n2)
n3 = str(input('Terceiro aluno:'))
print(n3)
n4 = str(input('Quarto aluno:'))
print(n4)
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi {}'.format(escolhido))
