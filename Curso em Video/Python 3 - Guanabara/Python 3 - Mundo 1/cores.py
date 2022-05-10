
# \033[0:33:44m 

# style                 # TEXT                   # BACK
# 0 - Nada              # 30 - Branco            # 40 - Branco
# 1 - Negrito           # 31 - Vermelho          # 41 - Vermelho
# 4 - Sublinhado        # 32 - Verde             # 42 - Verde
# 7 - Fundo             # 33 - Amarelo           # 43 - Amarelo
#                       # 34 - Azul              # 44 - Azul
#                       # 35 - Roxo              # 45 - Roxo
#                       # 36 - Azul Claro        # 46 - Azul Claro
#                       # 37 - Cinza             # 47 - Cinza



print('\033[1;31;43m Ola mundo!\033[m')

a = 3
b = 5
cores = {'limpa':'\033[m',
         'azul':'\033[34m',
         'amarelo':'\033[33m',
         'pretoebranco':'\033[7;30m',}
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}')
print('Os valores são {}{}{} e {}{}{}'.format('\033[32m', a,'\033[m', '\033[31m', b, '\033[m'))
print('Os valores são {} e {}'.format(cores['pretoebranco'], a, cores['limpa'], cores['amarelo'], b, cores['limpa']))