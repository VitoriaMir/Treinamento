# Jogo da Adivinhação

from random import choice 
from time import sleep
print('-=' * 28)
print('Vou pensar em um número entre 0 e 5. TENTE ADIVINHAR...')
print('-=' * 28)

num = int(input('\nEm que número eu pensei? '))

opcoes = [0, 1, 2, 3, 4, 5]
escolha = choice(opcoes)

print('PROCESSANDO...')
sleep(2)

if num == escolha:
    print('Empate escolhemos os mesmo número.')   
elif num > escolha:
    print(f'Você Ganhou! Eu pensei no {escolha}. Parabens')
else:
    print(f'GANHEI! Pensei no numero {escolha} e não no {num}')
# -----------------------------------------------------------------------------
"""
from random import randint 

print('-=' * 28)
print('Vou pensar em um número entre 0 e 5. TENTE ADIVINHAR...')
print('-=' * 28)

num = int(input('\nEm que número eu pensei? '))

opcoes = randint(0,5) # Faz o computador "PENSAR" 

print('PROCESSANDO...')
sleep(2)

if num == opcoes:
    print(f'Você Ganhou! Eu pensei no {opcoes}. Parabens')
else:
    print(f'GANHEI! Pensei no numero {opcoes} e não no {num}')
"""