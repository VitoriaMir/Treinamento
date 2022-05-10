# Primeiro e ultimo nome de uma pessoa

nome = str(input('Digite seu nome completo: ')).strip()

separa = nome.split()
pr_nome = separa[0]
ult_nome = (separa[len(separa)-1])

print('Muito prazer em te conhecer')
print(f'Seu primeiro nome é {pr_nome}')
print(f'Seu último nome é {ult_nome}')

