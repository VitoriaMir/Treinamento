# Abrindo e fechando arquivos

# Modo	    Símbolo	Descrição
# read              r           lê um arquivo existente
# write             w           cria um novo arquivo
# append            a           abre um arquivo existente para adicionar informações ao seu final
# update            +           ao ser combinado com outros modos, permite alteração de arquivo já existente (ex: r+ abre um arquivo existente e permite modificá-lo)

# 1. ELIMINAR LINHAS REPETIDAS:

# arquivocriado = open('criado.txt', 'w')  # para escrita ("w", de write)
arquivolido = open('2442561.txt', 'r')  # para leitura ("r", de read)

# dados = arquivolido.readlines()  # leitura de todas as linhas do arquivo
linhas_vista = set()

repetidas = []
for linha in arquivolido:
    if linha not in linhas_vista:
        #   arquivocriado.write(linha)
        linhas_vista.add(linha)
    else:
        repetidas.append(linha)


arquivolido.close()
# arquivocriado.close()
