# Comparando números

# Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:

# O primeiro valor é maior
# – O segundo valor é maior
# – Não existe valor maior, os dois são iguais

num1 = int(input('\033[1;33mPrimeiro número: \033[m'))
num2 = int(input('\033[1;35mSegundo número: \033[m'))


if num1 > num2:
    print('O primeiro valor é MAIOR')
elif num2 > num1:
    print('O segundo valor é MAIOR')
else:
    print('Não existe valor maior, os dois são iguais')
