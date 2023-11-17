# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar
# ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano = int(input('Ano de nascimento:'))
print(ano)
atual = date.today().year
idade = atual - ano
print('Quem nasceu em {} tem {} idade em {}'.format(ano, idade, atual))
if idade == 18:
    print('Você tem se alistar {}IMEDIATAMENTE{}'.format('\033[1;31m', '\033[m'))
elif idade < 18:
    saldo = 18 - idade
    print('Você ainda não tem 18 anos ainda faltam {} anos para o alistamento.'.format(saldo))
    print('Seu alistamento será em {}'.format(atual + saldo))
else:
    saldo = idade - 18
    print('Você deveria ter se alistado há {} anos'.format(saldo))
    print('Seu alistamento foi em {}'.format(atual - saldo))
