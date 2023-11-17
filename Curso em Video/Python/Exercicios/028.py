from random import randint
from time import sleep
computador = randint(0, 5)  # Faz o computador sortear um numero entre 0 a 5
print("-=-" * 20)
print('Vou pensar em um numero entre 0 á 5! Tente adivinhar!')
print('-=-'*20)
jogador = int(input('Em que numero eu pensei? '))
print(jogador)
print('PRICESSANDO...')
sleep(3)
if jogador == computador:
    print('PARABÉNS!! Você acertou!')
else:
    print('VOCÊ ERROU!! Eu pensei no numero {} e não no numero {}!'.format(computador, jogador))





