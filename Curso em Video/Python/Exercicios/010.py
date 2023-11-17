real = float(input('Quanto dinheiro você possui? R$'))
print(real)
dol = real / 3.75
print('Convertendo R${:.2f} para dolar, você possui US${:.2f} '.format(real, dol))
