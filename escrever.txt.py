with open('texto.txt', 'w') as arquivo:
    texto = list()
    texto.append('Amet ')
    texto.append('Ipsum ')
    texto.append('Lorem ')
    texto.append('Dolor ')
    texto.append('Sit ')

    arquivo.writelines(texto)
