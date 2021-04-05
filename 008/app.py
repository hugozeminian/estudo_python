# if else statement - ATENCAO na indentacao

tenho_sede = False

if tenho_sede:
    print("beber agua")
print("Vida que segue")

esta_frio = False

if esta_frio:
    print("Vestir um casaco")
else:
    print("Vestir camiseta")

tenho_sede = True
tenho_fome = False
dieta = True

if tenho_fome or tenho_sede:
    print("vou na cozinha")
else:
    print("ficar vendo o curso de python do Roger do canal Refatorando")

if tenho_fome and tenho_sede:
    print("vou na cozinha")
else:
    print("ficar vendo o curso de python do Roger do canal Refatorando")

if tenho_fome and tenho_sede:
    print("fazer sanduiche e coca")
elif not(tenho_fome) and tenho_sede:
    if dieta:
        print("tomar agua")
    else:
        print("tomar uma coca")
elif tenho_fome and not(tenho_sede):
    print("fazer um sanduiche")
else:
    print("ficar vendo o curso de python do Roger do canal Refatorando")

n1 = 5
n2 = 32

if n1 == n2:
    print("variaveis iguais")
elif n1 != n2:
    print("variaveis diferentes")
elif n1 > n2:
    print("n1 maior que n2")
elif n1 <= n2:
    print("n1 menor ou igual a n2")