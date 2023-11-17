"""nome = str(input('Qual é o seu nome? '))
print(nome)
if nome == 'Caroline':
    print('Que lindo nome você tem! ')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))"""

n1 = float(input('Digite uma nota: '))
print(n1)
n2 = float(input('Digite outra nota: '))
print(n2)
m = (n1 + n2) / 2
print('Sua media foi {:.1f} '.format(m))
if m >= 6.0:
    print('Sua media foi boa! PARABÉNS! ')
else:
    print('Sua media foi ruim! ESTUDE MAIS!')

# Um codigo que possui apenas um 'if' é uma estrutura condicional simples
# Um codigo que possui 'if' e 'else' é uma estrutura condicional composta
