# Exercício Python 31. Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas

dist = float(input('Qual é a distancia da sua viagem: '))
print(dist)
print('Você esta prestes a começar uma viagem de {}Km'.format(dist))
if dist <= 200:
    passagem = dist * 0.50
else:
    passagem = dist * 0.45
print('O preço da sua viagem será de R${:.2f}'.format(passagem))
