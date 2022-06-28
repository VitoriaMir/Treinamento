# Analisador de Textos

nome = str(input('Digite teu nome todo: ')).strip()

letras = (len(nome) - nome.count(' '))
separa = nome.split()

print('Seu nome é {} em maiúsculas'.format(nome.upper()))
print('Seu nome é {} em minúsculas'.format(nome.lower()))
print(f'Seu nome tem {letras} letras ao todo')
# print('E seu primeiro nome tem {} letras'.format(nome.find(' ')))
print('Seu primeiro nome é {} e ele tem {} letras'. format(separa[0], len(separa[0])))