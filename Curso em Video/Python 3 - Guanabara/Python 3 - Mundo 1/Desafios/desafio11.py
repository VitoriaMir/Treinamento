
# Pintando Parede
# Desafio 011
larg = float(input('Largura da parede: '))
altu = float(input('Altura da parede: '))

area = larg * altu
print(f'Sua parede tem a dimensão de {larg} x {altu} e sua área é de {area}m².')

tinta = area / 2
print(f'Para pintar essa parede, voce vai precisar de {tinta}l de tinta.')
"""
# -- --------------------------------------------------
"""
# Calculando Descontos
# Desafio 012
valor = float(input('Qual é o valor: '))
porcent = int(input('Qual é o desconto:'))
novo_preco = valor - (valor * porcent / 100)

print(f'O preço com desconto de {porcent}% é de {novo_preco:.2f}')
