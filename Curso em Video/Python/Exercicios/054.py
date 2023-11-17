# Crie um programa que leia o ano de nascimento de sete pessoas. No final,
# mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores

from datetime import date
totmaior = 0
totmenor = 0
for c in range(1, 8):
    ano = (int(input('Em que ano a {}° nasceu: \n'.format(c))))
    print(ano)
    atual = date.today().year
    idade = atual - ano
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Tivemos {} pesoas de maior'.format(totmaior))
print('Tivemos {} pessoas de menor'.format(totmenor))
