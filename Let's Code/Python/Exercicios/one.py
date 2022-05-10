# Escreva um programa que leia uma sequência de números inteiros e os salve em uma lista.
# Em seguida o programa deve ler um outro número inteiro C.
# O programa deve então encontrar dois números de posições distintas da lista cuja multiplicação seja C e imprimi-los.
# Caso não existam tais números, o programa deve imprimir uma mensagem correspondente. Exemplo:

# Lista = [2, 4, 5, 10, 7]
# C = 35
# Resultado: 5 e 7

# Lista = [2, 4, 5, 10, 7]
# C = 25
# Resultado: não existem tais números

lista = [2, 4, 5, 10, 7]
c = int(input('Digite um numero: '))
resul = []

for num in lista:
    var = c // num
    r = var * num
    if r == c:
        resul.append(var)
    elif r != c:
        continue

if len(resul) > 1:
    print(f'\n O resultado {resul}')
else:
    print('Não existem tais números')
