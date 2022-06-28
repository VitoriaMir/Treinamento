
# Aluguel de Carros
# Desafio 015
dias =  int(input('Quantos dias você usou: '))
kilm = float(input('Quantos km você usou: '))
carro = 60
km = 0.15

total = (dias * carro) + (kilm * km)

print(f'Você usou o carro por {dias} dias e rodou {kilm}KM, então o valor a ser pago é R${total:.2f}')
# -- --------------------------------------------------