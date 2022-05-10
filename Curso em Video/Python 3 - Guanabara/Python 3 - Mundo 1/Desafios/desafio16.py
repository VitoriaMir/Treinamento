# Quebrando um número
from math import trunc

valor = float(input('Digite um valor: '))

num = trunc(valor)      
#num = int(valor)      # Vai dar o mesmo resultado

print(f'O valor digitado foi {valor} e a sua porção inteira é {num}.')