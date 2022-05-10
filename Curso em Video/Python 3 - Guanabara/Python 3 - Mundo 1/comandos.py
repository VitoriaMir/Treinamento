#                           Operadores Aritmétricos


# Ordem de Precedência
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +, -

"""
nome = input('Qual é o seu nome? ')

print(f'Olá {nome}! Prazer em te conhecer!')
"""

"""
# Somar com int, para inteiros
num1 = int(input('Digite o primeiro numero? '))
num2 = int(input('Digite o segundo numero? '))
"""

# Somar com Float, para 
num1 = float(input('Digite o primeiro numero? '))
num2 = float(input('Digite o segundo numero? '))

soma = num1 + num2
subtrair = num1 - num2
multiplicar = num1 * num2
dividir = num1 / num2
exponenciacao = num1 ** num2
resto = num1 % num2
divisao_arredondado =  num1 // num2

print(f'A soma de {num1} + {num2} = {soma}')
print(f'A subtrair de {num1} + {num2} = {subtrair}')
print(f'A multiplicar de {num1} + {num2} = {multiplicar}')
print(f'A dividir de {num1} + {num2} = {dividir}')
print(f'A exponenciacao de {num1} + {num2} = {exponenciacao}')
print(f'A resto de {num1} + {num2} = {resto}')
print(f'A divisao com valor arredondado de {num1} + {num2} = {divisao_arredondado}')

# -- ------------------------------------------------------------------------------------