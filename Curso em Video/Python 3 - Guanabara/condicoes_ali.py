
nome = str(input('Qual é o seu nome? '))

if nome == 'Gustavo':
    print('Que nome bonito! ')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil. ')
elif nome in 'Ana Claúdia ':
    print('Belo nome feminino')
else: 
    print('Seu nome é bem normal.')
    print('Tenha um bom dia, {}'.format(nome))