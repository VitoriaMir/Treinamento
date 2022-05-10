
# Calculando Descontos
# Desafio 012
valor = float(input('Qual é o valor: '))
porcent = int(input('Qual é o desconto:'))
novo_preco = valor - (valor * porcent / 100)

print(f'O preço com desconto de {porcent}% é de {novo_preco:.2f}')
