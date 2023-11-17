# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.

# Ñ ESTA FUNCIONANDO

print('-='*10)
print('Gerador de PA')
print('-='*10)
primeiro = int(input('Primeiro termo:'))
print(primeiro)
razao = int(input('Razão: '))
print(razao)
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais? '))
        print(mais)
print('Progressão finalizada com {} termos mostrados.'.format(total))

