n = str(input('Nome completo: ')).strip()
print(n)
nome = n.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {} '.format(nome[0]))
print('Seu segundo nome é {} '.format(nome[len(nome)-1]))


