# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
from random import randint
from time import sleep

computador = randint(0, 10)
print("-=-" * 20)
print('Vou pensar em um numero entre 0 á 10! Tente adivinhar!')
print('-=-' * 20)
sleep(1)
acertou = False  # por enquanto o acerto é falso, mas assim que vc certar ele passa a ser verdadeiro
tentativas = 0
while not acertou:  # enquanto vc n acertar
    jogador = int(input('Em que número eu pensei? '))
    print(jogador)
    tentativas += 1  # se vc errar adiciona mais uma tentativa
    if jogador == computador:  # se o jogador acertar o número do computador ou se o número do jogador for igual ao do computador
        acertou = True  # a partir de o acertou passa a ser verdadeiro
        sleep(1)
    else:
        if jogador < computador:  # se o número do jogador foi menor q o número do computador
            print('Quase lá, tente um número maior')
        elif jogador > computador:
            print('Quase lá, tente um número menor')  # se o número do jogador foi maior q o número do computador
print('Finalmente você acertou')
print('Você teve {} tentativas'.format(tentativas))
