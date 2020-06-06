larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
area = larg * alt
print(f'Sua parede tem a dimensão de {larg:.2f}m X {alt:.2f}m e sua área é de {area:.2f}m².')
tinta = area / 2
print(f'Você precisa de {tinta:.2f} litros de tinta para pintá-la.')
