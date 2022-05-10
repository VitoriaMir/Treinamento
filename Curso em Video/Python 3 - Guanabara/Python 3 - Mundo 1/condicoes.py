# Condições Simples e Composta

#   if condition:       # SE
#        pass
#    else:              #SE NÃO
#        pass

"""
nome = str(input('Qual é o seu nome? '))

if nome == 'Vitória':
    print('Que nome lindo você tem!!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}'.format(nome))
"""

num1 = float(input('Digite a primeira nota: '))
num2 = float(input('Digite a segunda nota: '))
media = (num1 + num2) / 2
print(f'A sua média foi {media:.1f}')

# Condições Composto
"""
if media >= 6.0:
    print('Sua média foi boa! PARABÉNS')
else:
    print('Sua média foi ruim! ESTUDE MAIS')
"""
# Condições Simples
print('PARABÉNS' if media >=6 else 'ESTUDE MAIS')