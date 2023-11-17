# Faça um programa que jogue par ou ímpar com o computador.O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo

from random import randint
from time import sleep

v = 0
while True:
    jog = int(input('Digite um número para jogar: '))
    comp = randint(1, 11)
    total = jog + comp
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/N]')).upper().strip()[0]
    print(f'Você jogou {jog} e o computador jogou {comp}. Total de {total}', end=' ')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            print('Você venceu')
            v += 1
        else:
            print('Você perdeu')
            break
print('Vamos jogar novamente...')
