num = [2, 5, 9, 1, 6, 44]
num[2] = 3  # no indice 2, o número é alterado, no lugar do 9 fica o 3
num.append(7)  # adiciona o nº 7 na lista
num.insert(2, 8)  # adiciona um número na posição que eu quero, no caso no indice 2 add o nº 8
if 4 in num:  # se 4 estiver na lista num
    num.remove(4)  # remora o 4
else:
    print('Não achei o número 4')
'''num.remove(2)'''  # remore o número em ordem, se tiver 2 numeros iguais ele remove o q vem primeiro
num.sort()  # num.sort() coloca minha lista em ordem crescente
num.sort(reverse=True)  # coloca em ordem decrescente
del num[3]  # remove o elemento do indice 3
num.pop()  # remove o último elemento, essa função tb remove o elemneto se vc colocar o indice que vc deseja remover,
# por exemplo, num.pop(3)
num.remove(9)  # vai remover o elemento nove

print(num)
print(f'Essa lista tem {len(num)} elementos')  # len(num) conta quantos elementos tem na lista"""
