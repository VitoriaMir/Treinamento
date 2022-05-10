# Dada uma lista de inteiros, descubra o maior numero da lista, e quantas vezes ele se repete
# exemplos
# Input: [45,2,96,81,45,96,75,61,75,2,45,96,75]
# Output: [96, 3]

from ast import Num
from itertools import count


digits = [45,2,96,81,45,96,75,61,75,2,45,96,75]

for numero in digits:
    maior = max(digits)
    if maior :
        repete = digits.count(maior) 

print(numero)
