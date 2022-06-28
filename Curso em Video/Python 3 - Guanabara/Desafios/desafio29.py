# Radar eletrônico


velocidade = float(input('Qual é a velocidade atual do carro? '))

rapido = 7 * (velocidade - 80)

# Condição Simpificada
if velocidade > 80:
    print('MULTADO! Você excedeu o limite peritido que é de 80km/h')
    print(f'Você deve pagar uma multa de R${rapido}')

print('Tenha um BOM DIA! Dirija com segurança!')


