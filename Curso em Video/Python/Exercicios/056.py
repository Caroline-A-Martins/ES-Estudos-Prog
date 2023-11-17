# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
menor20 = 0
mediaidade = 0
maioridade = 0
somaidade = 0
homemvelho = ''
for p in range(1, 5):
    print('----------- {}º PESSOA -----------'.format(p))
    nome = str(input('Nome: '))
    print(nome)
    sexo = str(input('Sexo [M/F]:')).strip().lower()
    print(sexo)
    idade = int(input('Idade: '))
    print(idade)
    somaidade += idade
    if p == 1:
        somaidade = idade
    else:
        somaidade += idade
    if p == 1:
        homemvelho = nome
        maioridade = idade
    if idade > maioridade:
        maioridade = idade
        homemvelho = nome
    if sexo == 'F' and idade < 20:
        menor20 += 1
mediaidade = somaidade / 4
print('A medía de idade do grupo é de {} anos'.format(mediaidade))
print('Ohomem mais velho tem {} anos e se chama {}'.format(maioridade, homemvelho))
print('Nessa lista tem {} melher(es) menor(es) de idade'.format(menor20))
