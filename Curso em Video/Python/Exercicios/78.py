#  Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
#  No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.


""" MINHA SOLUÇÃO, PROBLEMA DELA É QUE SE TIVER DOIS VALORES IGUAIS ELA SÓ PEGA O QUE ESTÁ MAIS PERTO """
valores = list()

for cont in range(5):
    valores.append(int(input('Digite um valor: \n')))

print(f'Os valores digitados foram:{valores}')
print(f'O maior valor digitado foi {max(valores)} na posição {valores.index(max(valores))+1}')
print(f'O menor valor digitado foi {min(valores)} na posição {valores.index(min(valores))+1}')
print('-='*30)

"""SOLUÇÃO DO PROFESSOR"""

listanum = []
mai = []
men = []
for c in range(0,5):
    listanum.append(int(input(f'Digite um valor para a posição {c+1}: ')))
    if c == 0:
        mai = men = listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print()

print(f'Valores digitados: {listanum}')
print(f'O maior valor digitado foi {mai} nas posição ', end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f'{i + 1}, ', end='')
print()

print(f'O menor valor digitado foi {men} nas posição ', end='')
for i, v in enumerate(listanum):
    if v == men:
        print(f'{i + 1}, ', end='')
print()




