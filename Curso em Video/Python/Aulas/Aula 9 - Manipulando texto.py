'''Nessa aula, vamos aprender operações com String no Python. As principais operações que vamos aprender são o 
Fatiamento de String, Análise com len(), count(), find(), transformações com replace(), upper(), lower(), capitalize(
), title(), strip(), junção com join().'''

frase = "Curso em Video Python"
print(frase[3])

print(frase[3:13])

print(frase[:13])

print(frase[1:15])

print(frase[1:15:2])

print(frase[1::2])

print(frase.count('o'))

print(frase.upper().count('O'))

print(len(frase))

print(frase.replace('Python', 'Android'))

print(frase[0])

print('Curso' in frase)

print(frase.find('Curso'))

print(frase.split())

dividido = frase.split()
print(dividido[0])

dividido = frase.split()
print(dividido[2])
