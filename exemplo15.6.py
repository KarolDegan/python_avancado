def le_arquivo(nome_arquivo):
    for uma_linha in open (nome_arquivo, "r"):
        uma_linha = uma_linha.split(';')
        yield uma_linha[0], int(uma_linha[3])
        #yield uma_linha.rstrip()

arquivo = input("Nome do arquivo: ")
for linha in le_arquivo(arquivo):
    print(linha)

