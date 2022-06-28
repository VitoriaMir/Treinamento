# Analisando Triângulos v2.0
#
# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

pri = float(input('Primeiro segmento: '))
seg = float(input('Segundo segmento: '))
ter = float(input('Terceiro segmento: '))

if pri < seg + ter and seg < pri + ter and ter < pri +seg:
    print('Os segmentos acima PODEM FORMAR triângulo!')
    if pri == seg == ter:
        print('Os segmentos acima PODEM FORMAR triângulo EQUILÁTERO!')
    elif pri != seg != ter != pri:
        print('Os segmentos acima PODEM FORMAR triângulo ESCALENO!')
    elif pri != seg == ter or pri == seg != ter or pri == ter != seg:
        print('Os segmentos acima PODEM FORMAR triângulo ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODE FORMAR um triângulo!')

