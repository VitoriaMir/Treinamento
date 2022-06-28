# GAME: Pedra, Papel e Tesoura
# Crie um programa que faça o computador jogar Jokenpô com você.
import random
from time import sleep

print('Bem vindo ao Jogo de Pedra, Papel e Tesoura')
print('Vamos começar?')

print('Escolha uma das opções:')
print('[1] Pedra\n[2] Papel\n[3] Tesoura')
opcao = int(input('Qual é a sua jogada: \n'))

if opcao == 1:
    print('Você escolheu Pedra')
elif opcao == 2:
    print('Você escolheu Papel')
elif opcao == 3:
    print('Você escolheu Tesoura')
else:
    print('Opção inválida')

print('JO')
sleep(2)
print('KEN')
sleep(2)
print('PO')
sleep(2)

if opcao == 1 or opcao == 2 or opcao == 3:
    opcao_pc = random.randint(1, 3)
    if opcao_pc == 1:
        print('O computador escolheu Pedra')
    elif opcao_pc == 2:
        print('O computador escolheu Papel')
    elif opcao_pc == 3:
        print('O computador escolheu Tesoura')
    else:
        print('Opção inválida')

    if opcao == opcao_pc:
        print('Empate')
    elif opcao == 1 and opcao_pc == 2:
        print('Você ganhou')
    elif opcao == 1 and opcao_pc == 3:
        print('O computador ganhou')
    elif opcao == 2 and opcao_pc == 1:
        print('O computador ganhou')
    elif opcao == 2 and opcao_pc == 3:
        print('Você ganhou')
    elif opcao == 3 and opcao_pc == 1:
        print('Você ganhou')
    elif opcao == 3 and opcao_pc == 2:
        print('O computador ganhou')
    else:
        print('Opção inválida')
