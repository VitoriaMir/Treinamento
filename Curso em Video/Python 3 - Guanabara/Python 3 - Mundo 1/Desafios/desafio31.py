# Custo da Viagem

distancia = int(input('Qual é a distância da sua viagem? '))

viagem = distancia * 0.50
viagem_log = distancia * 0.45

if distancia <= 200:
    print(f'Você está preste a começar uma viagem de {distancia}KM')
    print(f'E o preço da sua passagem será de R${viagem}')
else:
    print(f'Você está preste a começar uma viagem de {distancia}KM')
    print(f'E o preço da sua passagem será de R${viagem_log}')

# ----------------------------------------------------------------------