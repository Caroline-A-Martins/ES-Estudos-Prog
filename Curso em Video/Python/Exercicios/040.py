# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma
# mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5,0: REPROVADO
# – Média entre 5,0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO


nota1 = float(input('Digite a primeita nota: '))
print(nota1)
nota2 = float(input('Digite a segunda nota: '))
print(nota2)
media = (nota1 + nota2)/2
print('Tiranfo {:.1f} e {:.1f}, sua média do alune é {:.1f}'.format(nota1, nota2, media))
if media >= 7:
    print('Você está APROVADO')
elif media == 5 and media < 7:
    print('Você está de RECUPERAÇÃO')
else:
    print('Você está REPROVADO')
