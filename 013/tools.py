# toda variavel pode ser alterada, sempre deve criada em minuscula
# por convensao, variaveis em maiusculas sao como se fosse constantes, nao devem ser alteradas
PI = 3.14
GRAVITY = 9.8


def get_extension(file):
    return file[file.index(".") +1:] # pega o nome do arquivo, dentro qual o indice do ponto, e pega do indice declarado +1 para frente, retornando entao a extensao

def highest_number(numbers):
    return max(numbers)