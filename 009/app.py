# loops

# while
print("** while **")
i = 1
while i <= 3:
    print(i)
    i += 1
print(f"terminou, contador = {i}")

# for
print("** for **")
familia = ["Hugo", "Louyse", "Julieta"]
#           0       1           2
for item in familia:
    print(item)

canal = "Refatorando"
for letra in canal:
    print(letra)

for index in range(10, 20, 2):
    print(index)

for index in range(len(familia)): #pegar valor do vetor
    print(index)
    print(familia[index])

for index in range(5):
    if index == 0:
        print("primeira linha")
    else:
        print(f"outras linhas {index}")

#Matriz
print("** matriz **")
matrix_numeros = [
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0],
]

for linha in matrix_numeros:
    #print(linha)
    print("-----")
    for coluna in linha:
        print(coluna)