# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e
# condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

preco = float(input('Valor total: R$'))
print(preco)
print('Formas de Pagamento \n'
      '[ 1 ] A vista dinheiro/cheque \n'
      '[ 2 ] A vista no cartao \n'
      '[ 3 ] Ate 2x no cartao \n'
      '[ 4 ] 3x ou mais no Cartao')

opt = int(input('Digite a forma de pagamento: '))
print(opt)
if opt == 1:
    final = preco - (preco * 0.10)
    print('Compra de R${:.2f} custara R${:.2f} no final'.format(preco, final))
    print('Desconto de R${:.2f}'.format(preco - final))
elif opt == 2:
    final = preco - (preco * 0.05)
    print('Compra de R${:.2f} custara R${:.2f} no final'.format(preco, final))
    print('Desconto de R${:.2f}'.format(preco - final))
elif opt == 3:
    total = preco
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${}'.format(parcela))
elif opt == 4:
    parcela = int(input('Quantas parcelas? \n'))
    final = preco + (preco * 0.20)
    print('Sua compra parcelada em {}x de R${:.2f} com JUROS de R${}'.format(parcela, (final / parcela), (final - preco)))
    print('Compra de R${:.2f} custara R${:.2f} no final'.format(preco, final))
else:
    print('Opcao escolhida invalida')
