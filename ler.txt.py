arquivo = open('loremipsum.txt').read()

print(arquivo)

print(arquivo.split('\n')[0])

print(arquivo[0:3])

with open('loremipsum.txt', 'r') as arquivoTexto:
    conteudo = arquivoTexto.read()
    print(conteudo)