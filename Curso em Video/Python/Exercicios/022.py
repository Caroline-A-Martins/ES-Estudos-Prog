nc = str(input('Digite seu nome completo: ')).strip()
print(nc)

print('Analizando seu nome ...')
print('Seu nome em letras maiusculas é {} '.format(nc.upper()))
print('Seu nome em letras minusculas é {} '.format(nc.lower()))
print('Seu nome tem ao todo {}'.format(len(nc) - nc.count(' ')))
separa = nc.split()
print('Seu primeiro nome é {} e ele tem {} letras '.format(separa[0], len(separa[0])))
