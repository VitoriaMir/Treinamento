# Sorteando uma ordem na lista

from random import shuffle

p = input('Primeiro Aluno: ')
s = input('Segundo Aluno: ')
t = input('Terceiro Aluno: ')
q = input('Quarto Aluno: ')

lista = [p, s, t, q]
shuffle(lista)

print(f'O aluno escolhido foi {lista}')

