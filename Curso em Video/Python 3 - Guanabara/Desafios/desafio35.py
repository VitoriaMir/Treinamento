# Analisando Triângulo

print('-=' * 15)
print(' Analisando Triângulos')
print('-=' * 15)

pri = float(input('Primeiro segmento: ')) 
seg = float(input('Segundo segmento: '))
ter = float(input('Terceiro segmento: '))

if pri < seg + ter and seg < pri + ter and ter < pri +seg:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODE FORMAR um triângulo!')