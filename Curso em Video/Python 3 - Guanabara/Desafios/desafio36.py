# Aprovando Empréstimo

"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""

valor = float(input('Valor da casa: R$'))
salario = float(input('Salario do comprador: R$'))
finan = int(input('Quantos anos de financiamento? '))

prestação = valor / (finan * 12)
minimo = salario * (30 / 100)

print(f'Para pagar uma casa de R${valor} em {finan} anos a prestação será de R${prestação:.2f}')

if prestação <= minimo:
    print('Emprestimo CONCEDIDO')
else:
    print('Emprestimo NEGADO')

