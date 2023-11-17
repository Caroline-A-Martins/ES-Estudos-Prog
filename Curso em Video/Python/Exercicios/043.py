# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
# de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida


peso = float(input('Seu peso:(Kg)'))
print(peso)
altura = float(input('Sua altura: (m) '))
print(altura)
imc = peso / (altura**2)
print('O IMC dessa pessoa é {:.2f}'.format(imc))
if imc < 18.5:
    print('TENHA CUIDADO! Você está Abaixo do peso.')
elif 18.5 <= imc < 25:
    print('PARABÉNS! Você está com Peso ideal.')
elif 25 <= imc < 30:
    print('FIQUE ATENTO! Você está com Sobrepeso.')
elif 30 <= imc <= 40:
    print('FIQUE ATENTO! Você está com Obesidade')
else:
    print('TOME CUIDADO! Você está com Obesidade Mórbida')

