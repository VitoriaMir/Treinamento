# Escreva um programa que leia duas sequências de n e m valores inteiros, onde n ≤ m, e imprima
# quantas vezes a primeira sequência ocorre na segunda.
# Exemplo:
#       Primeira sequência: 1 0 1
#       Segunda sequência: 1 1 0 1 0 1 0 0 1 1 0 1 0
#       Resultado: 3

from itertools import count

n = '101'
m = '1101010011010'

if n <= m:
    print(m.count(n))