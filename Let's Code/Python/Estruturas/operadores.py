#                                   Operadores aritméticos

# Podemos fazer operações aritméticas simples
a = 2 + 3  # Soma
b = 2 - 3  # Subtração
c = 2 * 3  # Multiplicação
d = 2 / 3  # Divisão
e = 2 // 3  # Divisão inteira
f = 2 ** 3  # Potência
g = 2 % 3  # Resto de divisão

print(a, b, c, d, e, f, g)

# Podemos fazer operações dentro do print

print(a + 1, b + 1)

# Podemos fazer operações com variáveis não inteiras
nome = input('Digite seu primeiro nome:')
nome = nome + ' Schmitt'
print(nome)

#                           Operadores relacionais
comparacao1 = 5 > 3
print(comparacao1)
comparacao2 = 5 < 3
print(comparacao2)

# Maior que: >
# Maior ou igual: >=
# Menor que: <
# Menor ou igual: <=
# Igual: ==
# Diferente: !=

#                           Operadores lógicos

# and: verdadeiro se condição 1 for verdadeira e condição 2 for verdadeira
# or: verdadeiro se condição 1 for verdadeira ou condição 2 for verdadeira

comparacao1 = 5 > 3 and 6 > 3
comparacao2 = 5 < 3 and 6 > 3

comparacao3 = 5 > 3 or 6 > 3
comparacao4 = 5 < 3 or 6 > 3

# Se:
comparacao5 = 5 > 3  # é verdadeira,
comparacao6 = not (5 > 3)  # será falsa,
