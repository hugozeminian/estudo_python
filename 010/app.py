# Colecoes: set e dictionary
# SET
# utiliza {}, 
# nao contabiliza itens repetidos
# lista nao ordenada

# LISTA utiliza []

frutas = {"maca", "laranja", "abacaxi"}

frutas.add("pera")
print(frutas)
frutas.remove("maca")
print(frutas)
frutas.pop() #como a lista nao eh ordenada ele nao remove o ultimo, mas sim um valor qualquer
print(frutas)

set1 = {"maca", "laranja", "abacaxi"}
set2 = {0,3,50,-74}
set3 = {True, False, False, False}
set4 = {"Hugo", 33, True}

print(set4)
print(len(set4))