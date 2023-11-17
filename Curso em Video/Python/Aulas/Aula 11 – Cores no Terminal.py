print('\033[0;30;41mOlá, Mundo\033[m')

print('\033[1;97;45mOlá, Mundo\033[m')

print('{}Olá, Mundo{}'.format('\033[4;34m', '\033[m'))

a = 3
b = 5
print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m'.format(a, b))

nome = 'Caroline'
print('Muito prazer em te conhecer {}{}{}'.format('\033[4;34m', nome, '\033[m'))

nome = 'Caroline'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7;97m'}

print('Muito prazer em te conhecer {}{}{}'.format(cores['pretoebranco'], nome, cores['limpa']))
