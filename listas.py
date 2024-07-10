lista_mesclada = [1, 2, 3, "Olá, Python", True, 12.6]
print(lista_mesclada)
lista_mesclada.append(["Lista aninhada"])
print(lista_mesclada)
lista_mesclada.insert(4, 5)
print(lista_mesclada)
print(len(lista_mesclada))
lista_mesclada.remove(2)
print(lista_mesclada)

nova_lista_mesclada = []

for index in range(0, 5):
    nova_lista_mesclada.append(lista_mesclada[index])

print(nova_lista_mesclada)