# Gerenciador de Pagamento

#  Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de
#  pagamento:
#
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('-----------LOJAS DA VITORIA-----------')
preco = float(input('Digite o valor do produto: '))
print('\n[1] À vista no dinheiro ou cheque, 10% de desconto.\n'
      '[2] À vista no cartão, 5% de desconto.\n'
      '[3] Em até 2x no cartão, preço formal.\n'
      '[4] 3x ou mais no cartão, 20% de juros.')

forma = int(input('Digite a forma de pagamento: '))

if forma == 1:
    valor = preco - (preco * 0.10)  # valor - (valor * 10 / 100)
    print(f'\nO valor a ser pago é de R${valor:.2f}')
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f} no final.')
elif forma == 2:
    valor = preco - (preco * 0.05)  # valor - (valor * 5 / 100)
    print(f'\nO valor a ser pago é de R${valor:.2f}')
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f} no final.')
elif forma == 3:
    print(f'\nO valor a ser pago é de R${preco:.2f}')
    print(f'Sua compra de R${preco:.2f} vai custar R${preco:.2f} no final.')
elif forma == 4:
    valor = preco + (preco * 0.20)  # valor + (valor * 20 / 100)
    total = int(input('\nDigite quantas vezes o pagamento será feito: '))
    parcelas = valor / total
    print(f'\nSua compra será parcelada em {total}x de R${parcelas:.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${valor:.2f} no final.')
else:
    print('Opção inválida')
    