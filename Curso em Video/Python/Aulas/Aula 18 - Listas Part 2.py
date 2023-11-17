teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)

galera2 = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera2[0])
print(galera2[0][0])
print(galera2[1][0])
print(galera2[2][1])

for pes in galera2:
    print(pes)
print()
for pes in galera2:
    print(f'Pessoas: {pes[0]}')
print()
for pes in galera2:
    print(f'Idade: {pes[1]}')
print()
for pes in galera2:
    print(f'{pes[0]} tem {pes[1]} anos de idade')
print()

galera3 = list()
dado = list()
totmai = totmen = 0
for c in range(3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera3.append(dado[:])
    dado.clear()

for p in galera3:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print()
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

