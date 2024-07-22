import time

with open('farAway.txt', 'r') as arquivo:
    linhas = arquivo.read().strip()
    palavras = linhas.split(' ')
    palavras.sort()

with open('farAwayOrdenado.txt', 'w') as arquivo:
    arquivo.write(' '.join(palavras))
