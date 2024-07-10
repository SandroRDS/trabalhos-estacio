dicionario =  {
    1: {
        'nome': 'Maria',
        'idade': 26,
        'nacionalidade': 'brasileira',
    },
}

dicionario.update({
    2: {
        'nome': 'Rafael',
        'idade': 22,
        'nacionalidade': 'estadunidense',
    },
    3: {
        'nome': 'Issac',
        'idade': 30,
        'nacionalidade': 'argentino',
    },
    4: {
        'nome': 'Matheus',
        'idade': 26,
        'nacionalidade': 'venezuelano',
    },
    5: {
        'nome': 'Italo',
        'idade': 20,
        'nacionalidade': 'boliviano',
    },
    6: {
        'nome': 'Marcos',
        'idade': 29,
        'nacionalidade': 'canadense',
    },
})

print(dicionario)

novoDicionario = dicionario.copy()

dicionario.pop(1)

print(dicionario)

dicionario.popitem()

print(dicionario)

dicionario.clear()
novoDicionario.clear()

novoDicionario2 = dict.fromkeys((1, 2, 3), 'valor repetido')
print(novoDicionario2.items())
print(novoDicionario2.keys())
print(novoDicionario2.values())
