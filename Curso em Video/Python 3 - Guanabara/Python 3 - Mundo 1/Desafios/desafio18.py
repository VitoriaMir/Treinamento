# Seno, Cosseno e Tangente
import math
angu = float(input('Digite o ângulo que você deseja: '))

cosseno = math.cos(math.radians(angu))
seno = math.sin(math.radians(angu))
tangente = math.tan(math.radians(angu))

print(f'O ângulo de {angu} tem o Seno de {seno:.2f}')
print(f'O ângulo de {angu} tem o Coseno de {cosseno:.2f}')
print(f'O ângulo de {angu} tem o Seno de {tangente:.2f}')