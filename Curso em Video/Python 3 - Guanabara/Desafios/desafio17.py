# Catetos e Hipotenusa

import math

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
# hi = (oposto ** 2 + adjacente ** 2) ** (1 / 2) # Jeito sem usar o math.hypot
hipot = math.hypot(oposto,adjacente)

print(f'A hipotenusa vai medir {hipot:.2f}.')