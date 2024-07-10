meu_dicionario = {
    1: {
        'codigo': 1,
        'linguagem': 'Python',
    },
    2: {
        'codigo': 2,
        'linguagem': 'Java',
    },
    3: {
        'codigo': 3,
        'linguagem': 'PHP',
    },
}

print(meu_dicionario)

print(type(meu_dicionario))

print(meu_dicionario.get(1).get('linguagem'))

print(len(meu_dicionario))

dicionario_frutas = {
    1: dict(nome = 'limão', tipo = 'ácida'),
    2: dict(nome = 'laranja', tipo = 'ácida'),
    3: dict(nome = 'manga', tipo = 'semiácida'),
    4: dict(nome = 'maçã', tipo = 'semiácida'),
    5: dict(nome = 'banana', tipo = 'doce'),
    6: dict(nome = 'mamão', tipo = 'doce'),
}

print(f'Fruta 1 -> Nome: {dicionario_frutas.get(1).get('nome')} | Tipo: {dicionario_frutas.get(1).get('tipo')}')
print(f'Fruta 2 -> Nome: {dicionario_frutas.get(2).get('nome')} | Tipo: {dicionario_frutas.get(2).get('tipo')}')

for index, fruta in dicionario_frutas.items():
    print(f'Nome: {fruta.get('nome')} | Tipo: {fruta.get('tipo')}')