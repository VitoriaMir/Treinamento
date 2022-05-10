# Sorteando um item na lista
from random import choice 

p = input('Primeiro Aluno: ')
s = input('Segundo Aluno: ')
t = input('Terceiro Aluno: ')
q = input('Quarto Aluno: ')

lista = [p, s, t, q]
escolha = choice(lista)

print(f'O aluno escolhido foi {escolha}')