larg = float(input('Largura da sua parede: '))
print(larg)
alt = float(input('Altura da sua parede: '))
print(alt)
area = larg * alt
print('Sua parede tem a dimensão de {}x{} e a área de {}m2 '.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede você precisa de {}L de tinta '.format(tinta))