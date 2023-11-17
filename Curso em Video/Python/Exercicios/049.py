# Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

tabuada = int(input('Digite um numero para ver sua tabuada:'))
print(tabuada)
for tab in range(1, 11):
    print('{} x {:2} = {:2}'.format(tab, tabuada, tabuada*tab))
