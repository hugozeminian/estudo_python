# Tratando excecao - Try, except, Finally

try: #tenta executar o comando, caso nao seja possivel ele ira executar as EXCEPTs abaixo
    numero = int(input("Digite um numero: "))
    10/numero
    print(numero)
except ZeroDivisionError:
    print("Divisao por zero nao e possivel")    #exemplo ao ser digitado zero 
except ValueError:
    print("digite um valor valido") #exemplo ao ser digitado um nome
except:
    print("erro inesperado") #exemplo ao tentar imprimir uma variavel inexistente
finally: #independente se o comando executado no TRY der certo ou ir para o EXCEPT, ele executara p FINALLY
    print("sempre executa")
