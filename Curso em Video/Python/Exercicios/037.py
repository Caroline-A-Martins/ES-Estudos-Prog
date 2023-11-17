# Exercício Python 37: Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário
# escolher qual será a base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.

num = int(input('Digite um numero: '))
print(num)
print('Escolha uma das bases de conversão:')
print('[1] Binario')
print('[2] Octal')
print('[3] Hexadecimal')
opcao = int(input('Sua opção foi: '))
print(opcao)
if opcao == 1:
    print('{}, convertido em {}BINARIO{} é {}'.format(num, '\033[1;32m', '\033[m', bin(num)[2:]))
elif opcao == 2:
    print('{}, convertido em {}OCTAL{} é {} '.format(num, '\033[1;35m', '\033[m', oct(num)[2:]))
elif opcao == 3:
    print("{}, convertido em {}HEXADECIMAL{} é {}".format(num, '\033[1;36m', '\033[m', hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
