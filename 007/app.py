#funcao ou metodo em Python, sempre deve iniciar com DEF (definition)

"""
def big_mac():
    print("sanduiche big mac")

print("inicio")
big_mac()
print("fim")
"""

def fazer_big_mac(nome):
    print(f"sanduiche big mac {nome}")

def fazer_batata(tamanho):
    print(f"batata {tamanho}")

def preparar_refri(tipo, tamanho):
    print(f"{tipo} {tamanho}")

#fazer_big_mac("Hugo")
#fazer_big_mac("Louyse")
#fazer_big_mac("Juju")

fazer_big_mac("Hugo")
fazer_batata("Grande")
preparar_refri("Coke", "Media")

def fazer_combo(nome, tamanho_batata, tipo_refri, tamanho_refri):
    print(f"***Saindo um combo")
    fazer_big_mac(nome)
    fazer_batata(tamanho_batata)
    preparar_refri(tipo_refri, tamanho_refri)

fazer_combo("HUGO", "Gigante", "Fanta", "Enorme")

def maior_num(lista_num):
    lista_num.sort()
    lista_num.reverse()
    maior_num = lista_num[0]
    return maior_num

res = maior_num([123,21,45,84984,-1,48,99999])
print(res)
