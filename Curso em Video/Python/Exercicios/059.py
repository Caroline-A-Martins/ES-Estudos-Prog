# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.

n1 = int(input('Digite um valor: '))
print(n1)
n2 = int(input('Digite outo valor: '))
print(n2)
print('--' * 10)
opcao = 0
while opcao != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opcao = int(input('Qual a sua opção: '))
    print(opcao)
    print('--' * 10)
    if opcao == 1:
        soma = n1 + n2
        print('Resultado de {} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        multi = n1 * n2
        print('Resultado de {} x {} = {}'.format(n1, n2, multi))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print('Entre {} e {} o maior é {}'.format(n1, n2, maior))
    elif opcao == 4:
        n1 = int(input('Digite um valor: '))
        print(n1)
        n2 = int(input('Digite outo valor: '))
        print(n2)
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção invaida.')
print('Fim do programa. ')
