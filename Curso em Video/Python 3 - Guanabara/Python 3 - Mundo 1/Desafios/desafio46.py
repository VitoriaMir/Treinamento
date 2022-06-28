# Contagem regressiva
# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0,
# com uma pausa de 1 segundo entre eles.
from time import sleep
import emoji as emoji

print('Contagem regressiva para o estouro de fogos de artifício')
for c in range(10, -1, -1):
    print(c)
    sleep(1)

print(emoji.emojize("BUM! BUM! POOOW!:fireworks::sparkler::tada:", use_aliases=True))
print('Fim do programa')
