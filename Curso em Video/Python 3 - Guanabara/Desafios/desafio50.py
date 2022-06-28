# Soma dos pares
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.
soma = 0
cont = 0
for c in range(0, 6 + 1):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += num
        cont += 1

print(f'A quantidade de números pares é {cont} e a soma dos números pares é {soma}')
