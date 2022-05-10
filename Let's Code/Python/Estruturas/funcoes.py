#                                          Funções - "subprograma"

def hello():
    print("Olá, mundo!")


def ola(nome):
    print("Olá", nome)


ola("Maria")
# Saída: Olá, Maria

aluno = "João"
ola(aluno)


# Saída: Olá, João


def dadosPessoais(nome, idade, cidade):
    print("Seu nome é {}, você tem {} anos e mora em {}.".format(nome, idade, cidade))


dadosPessoais("José", 30, "Maceió")
# Saída: Seu nome é José, você tem 30 anos e mora em Maceió.

dadosPessoais(idade=56, cidade="Florianópolis", nome="Ana")


# Saída: Seu nome é Ana, você tem 56 anos e mora em Florianópolis.

#                                          Funções com resposta

def somatorio(lista):
    soma = 0
    for item in lista:
        soma = soma + item
    return soma


numeros = [1, 2, 3, 4, 5]
soma_dos_numeros = somatorio(numeros)
print("A soma dos elementos da lista vale: ", soma_dos_numeros)

if somatorio(numeros) > 50:
    print("Que soma grande!")
else:
    print("Que soma pequena!")

'''
Saída:
A soma dos elementos da lista vale:  15
Que soma pequena!
'''


#                                          Funções recursivas

def funcaoRecursiva(numero):
    if numero != 1:
        funcaoRecursiva(numero - 1)
    print(numero)


print("Testando a função recursiva:")
funcaoRecursiva(10)


#                                          Agrupando parâmetros

def piscina(*infos):
    vol = infos[0] * infos[1] * infos[2]
    return vol


volume = piscina(5, 4, 5)

print('O volume é: ', volume)


def piscina(prof, largura, comprimento):
    vol = prof * largura * comprimento
    return vol


lista = [5, 4, 5]

volume = piscina(*lista)

print('O volume é: ', volume)


#                                          Parâmetros opcionais

def piscina(prof, **infos):
    vol = prof * infos['largura'] * infos['comprimento']
    return vol


volume = piscina(5, largura=4, comprimento=5)

print('O volume é: ', volume)


def piscina(prof, largura=4, comprimento=5):
    vol = prof * largura * comprimento
    return vol


infos = {'largura': 10, 'comprimento': 20}

volume = piscina(5, **infos)

print('O volume é: ', volume)
