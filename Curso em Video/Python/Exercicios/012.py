pre = float(input('Qual o preço do produto: R$'))
print(pre)
valor = pre - (pre * 5 / 100)

print('Seu produto custa R${:.2f} com a promoção de 5% vai custar é R${:.2f}'.format(pre, valor))
