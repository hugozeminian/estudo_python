# Como manipular arquivos em Python - ler, criar, alterar e deletar arquivos

# open("caminho", "r") -> passar 2 parametros = caminho do arquivo, modo como o arquivo serah aberto (pode ser dividido em 5 modos, vide abaixo)

# Mode
# r - leitura
# a - Append / incrementar no arquivo
# w - escrita (deleta o que existe no arquivo e coloca a nova informacao declarada  ou ja cria e escreve no arquivo novo)
# x - criar arquivo
# r+ - leitura + escrita

# o arquivo aberto deve ser armazanado em uma variavel
# dica - sempre que utilizar a funcao open, ja criar o arquivo.close() para nao correr risco dele ficar aberto.

# arquivo = open("012/test3.txt", "x")

# print(arquivo.readable()) # verifica se o arquivo esta habilitado para leitura
# print(arquivo.read()) # le o arquivo todo
# print(arquivo.readline()) # le a primeira linha do arquivo, se repetir o comado, a segunda linha e assim por diante.
# print(arquivo.readline())

# pega todas as linhas que tem no arquivo e transforma em uma lista
# lista = arquivo.readlines()

# print(lista)

# print(lista[3])

# arquivo.write("Python\n")

# arquivo.close()

# Excluindo arquivos
import os
# os.remove("012/test2.txt")
if os.path.exists("012/test2.txt"):
    os.remove("012/test2.txt")
else:
    print("Aula nao existe")


# Remover pasta (so funciona com a pasta vazia)
os.rmdir("012/nova_pasta")
