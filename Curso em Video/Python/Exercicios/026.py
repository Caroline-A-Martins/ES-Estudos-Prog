frase = str(input('Digite uma frase :')).strip().upper()

n1 = frase.count('A')
n2 = frase.find('A')+1
n3 = frase.rfind('A')+1
print('Numero de As: {} '.format(n1))
print('Posição que ele aparece pela primeira vez: {} '.format(n2))
print('Posição que ele aparece pela ultima vez: {} '.format(n3))
