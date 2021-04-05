#Collections, Lists and Tubles - colecao de dados

familia = ["Hugo", "Louyse", "Julieta"] #listas podem ser feitas com qualquer tipo de dado, bool, int, float, string

print(familia[0]) #primeiro dado
print(familia[-1]) #ultimo dado
print(familia[0:2]) #intervalo de dado, sem exclui o ultimo dado do vetor, neste caso Julieta
print(familia[1])

print(familia)
familia[2] = "Juju " #modificando o valor de um vetor
print(familia)

familia.extend(["Seraaaaaa?","Na mao de Deus"]) #adicionando valor no vetor
print(familia)

familia.insert(1, "Spock") #inserindo um novo vetor e direcionando a sua posicao ( as outras vao para frente )
print(familia)

familia.pop() #remove o ultimo vetor
print(familia)

familia.remove("Spock") #remove vetor especifico
print(familia)  

familia.clear() #limpa lista
print(familia)

familia = ["Hugo", "Hugo", "Louyse", "Julieta"]
print(familia.count("Hugo")) #Contar quantas vezes o valor se repete na lista de vetores

idade_familia = [33, 29, 6]
print(idade_familia)

idade_familia.sort() #ordena os valores dos vetores em ordem ascendente
print(idade_familia)
familia.sort()
print(familia)

idade_familia.reverse() #digita de tras para frente os vetores
print(idade_familia)
familia.reverse()
print(familia)

print("copia de vetores")
familia2 = familia.copy() #gerar uma nova variavel com uma copia de outra variavel 
familia.remove("Julieta")
print(familia)
print(familia2) 

#tople - nao pode ser alterado
coordenadas1 = [-49, -36]
coordenadas2 = (-49, -36) #toble
coordenadas1.pop
print(coordenadas1)
#coordenadas2.pop #### por ser tople, nao e possivel remover o vetor
print(coordenadas2)