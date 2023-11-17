nome = str(input('Qual é o seu nome? '))
print(nome)
if nome == 'Caroline':
    print('Que nome bonito!')
elif nome == 'Valentina' or nome == 'Enzo':
    print('Seu nome é bem comum no Brasil.')
elif nome in 'Ana Claudia Maria Julia':
    print('Belo nome feminino!')
# O else nesse caso não é obrigatorio, pois caso não seja nenhuma das opções acima o programa vai imprimir o ultimo
# print
else:
    print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))

# Um codigo que possui 'if','elif' e 'else' é uma estrutura condicional aninhada
