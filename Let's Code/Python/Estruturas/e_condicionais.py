#                                           IF - testa uma condição

idade = int(input('Digite sua idade:'))
if idade >= 12:
    print('Você pode entrar na montanha russa.')
print('Obrigado por participar.')

altura = float(input('Digite sua altura, em metros:'))
if idade >= 12 and altura >= 1.60:
    print('Você pode entrar na montanha russa.')
print('Obrigado por participar.')

#                                           ELSE - executa uma ação caso a condição não seja satisfeita

idade = int(input('Digite sua idade:'))
altura = float(input('Digite sua altura, em metros:'))
if idade >= 12 and altura >= 1.60:
    print('Você pode entrar na montanha russa.')
else:
    print('Você não pode entrar na montanha russa.')
print('Obrigado por participar.')

# É possível "aninhar" diversos if's e else's.
# O programa abaixo só deixa a pessoa entrar no brinquedo se tiver idade e altura mínimas:

idade = int(input('Digite sua idade:'))
if idade >= 12:
    resposta = input('Você gostaria de entrar nesta montanha russa?')
    if resposta == 'sim':
        print('Por favor, entre!')
    else:
        print('Ok então')
else:
    print('Você não tem idade suficiente para entrar nesse brinquedo.')

#                                           ELIF - executa uma ação caso a condição seja satisfeita

exercicios = int(input('Quantos exercícios de Python vc já fez?'))

if exercicios > 30:
    print('Já está ficando profissional!')
elif exercicios > 20:
    print('Tá indo bem, bora fazer mais alguns!')
elif exercicios > 10:
    print('Vamos tirar o atraso?')
else:
    print('Xiiii...')

