minha_string = "   Texto texto texto textO   "
                #1234567890123456789212345678 
print(type(minha_string))
print(minha_string)

print(minha_string.upper())
print(minha_string.lower())
print(minha_string.isupper()) #informa se é maiusculo
print(minha_string.islower()) #ubfirna se é minusculo
print(minha_string.strip()) #remove espaços no começo e no final
print(minha_string.replace("texto", "meu", 1)) #substitui, pode ser informado a quantidade
print(minha_string[21]) #em formato de vetor, é possível selecionar o caractere da string (passa o índice e retorna a string)  
print(minha_string[-7:-2]) #mesmo que o anterior, mas de trás para frente. (ultimo caractere é -1)
print(minha_string.index("xto")) #passa a string e retorna o índice
x = "xto" in minha_string # verificar se o texto existe (pode ser utilizado antes do índice)
print(x)

# quebrar linha de string
minha_string = """ linha1
linha2
linha3
"""
print(minha_string) 

minha_string = "linha4, \n linha5, \n linha 6."
print(minha_string)