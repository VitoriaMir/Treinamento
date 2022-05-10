#                                       Arquivos em Python

# Abrindo e fechando arquivos

# Modo	    Símbolo	Descrição
# read              r           lê um arquivo existente
# write             w           cria um novo arquivo
# append            a           abre um arquivo existente para adicionar informações ao seu final
# update            +           ao ser combinado com outros modos, permite alteração de arquivo já existente (ex: r+ abre um arquivo existente e permite modificá-lo)

# Devemos fechar o nosso arquivo usando a função close. Essa etapa é importante por 2 motivos:

#   Se alteramos o arquivo mas não o fechamos, as alterações não serão salvas;
#   Se esquecemos de fechar um arquivo, outros programas podem ter problemas ao acessá-lo.

# 1. Abrir ou criar um arquivo:
arquivocriado = open("criado.txt", "w")  # para escrita ("w", de write)

arquivolido = open("teste.txt", "r")  # para leitura ("r", de read)

# 2. Carregar os dados do arquivo (leitura)
dados = arquivolido.read()  # A função read() retorna todo o conteúdo do arquivo como uma string.
print(dados)

# 3. Manipular os dados do arquivo (escrita)
arquivocriado.write("linha 1")
arquivocriado.write("linha 2")
arquivocriado.write("linha 3")

# 4. Fechar o arquivo
arquivocriado.close()
arquivolido.close()

#                                       Comando with

with open('teste.txt', 'r') as arquivolido:
   dados = arquivolido.read()
   print(dados)

# É possível ler o arquivo linha a linha, como no exemplo:
with open('teste.txt', 'r') as arquivolido:
   linha = arquivolido.readline()
   while linha != '':
       print(linha, end='')
       linha = arquivolido.readline()

#                   OU

with open('teste.txt', 'r') as arquivolido:
    for linha in arquivolido:
        print(linha, end='')

# O mesmo pode ser feito para escrever no arquivo:
with open('teste.txt', 'r') as arquivolido:
    with open('copiateste.txt', 'w') as arquivocriado:
        for linha in arquivolido:
            arquivocriado.write(linha)


