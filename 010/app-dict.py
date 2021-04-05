# dicionario
# colecao utiliza chave e valor {"",""}
# nao sao ordenados (nao possui index)
# nao aceita valor duplicado
# ele eh modificavel

meses = {
    "Jan": "Janeiro",
    "Fev": "Fevereiro",
    "Mar": "Marco",
    "Abr": "Abril",
    "Mai": "Maio",
    "Jun": "Junho",
    "Jul": "Julho",
    "Ago": "Agosto",
    "Set": "Setembro",
    "Out": "Outrubro",
    "Nov": "Novembro",
    "Dez": "Dezembro",
}

print(meses["Jan"])
# print(meses("ABC")) - ira quebrar
print(meses.get("Fev"))
print(meses.get("ABC"))  # informa que nao existe ABC
# caso nao encontre a palavra, ele ira trazer o PADRAO (no caso Janeiro)
print(meses.get("ABC", "Janeiro"))
print(meses.get("Dez", "Janeiro"))

print(len(meses))