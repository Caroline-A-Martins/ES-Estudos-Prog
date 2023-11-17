# Exercício Python 29: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma
# mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
#Esse exercicio tambem pode ser feito com uma estrutura simples (apenas com um if), mas por algum motivo o meu
#programa não está aceitando.
km = float(input('Qual a velocidade do carro durante a viagem? '))
print(km)
if km > 80:
    print('Você ultapassou o limete de velocidade! Infelizmente você recebera uma multa.')
    multa=(km-80)*7
    print('Você terá que pagar R${:.2f}!'.format(multa))
else:
    print('Muito bem, você não ultrapassou o limite de velocidade')
