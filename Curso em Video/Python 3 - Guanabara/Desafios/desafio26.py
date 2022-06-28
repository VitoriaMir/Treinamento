# Primeira e a última ocorrência de uma string

frase = str(input('Digite uma frase: ')).lower().strip()

vezes = frase.count('a')
posiçao1 = frase.find('a')
posiçao2 = frase.rfind('a')

print(f'A letra A apareceu {vezes} na frase')
print(f'A primeira letra A apareceu na posição {posiçao1}')
print(f'A útima letra A apareceu na posição {posiçao2}')
