# Maior e menor valores

from re import A


p = int(input('Primeiro valor: '))
s = int(input('Segundo valor: '))
t = int(input('Terceiro valor: '))

menor = t
if p < s and p < t :
    menor = p
if s < p and s < t :
    menor = s

maior = t
if p > s and p > t :
    maior = p
if s > p and s > t :
    maior = s

print(f'O menor valor digitado foi {menor}')
print(f'O menor valor digitado foi {maior}')