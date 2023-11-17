# Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.


sexo = str(input('Informe seu genero:[F/M} ')).strip().upper()[0]
print(sexo)
while sexo not in 'FfMm':
    sexo = str(input('Dados invalidos. Informe seu genero:[F/M} ')).strip().upper()[0]
    print(sexo)
print('O genero {} foi registrado com sucesso.'.format(sexo))
