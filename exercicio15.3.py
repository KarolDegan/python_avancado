def qt_fatorial():
    num, fat = 0, 1
    while True:
        i = (yield num, fat)
        num += 1
        fat *= num #nessa ordem
        if i is not None:
            num = i # reinicia o valor do num e do fat
            fat = 1
            for a in range(1, num+1):
                fat *= a

qtde = int(input('Digite a quantidade de fatoriais: '))
gen = qt_fatorial()
print(next(gen)) #inicializa a função para poder usar o send

prim = int(input('\nDigite valor inicial para a próxima sequência: '))

while prim >= 0:
    r = gen.send(prim)# apenas 1 valor enviado
    fatoriais = [r]# criando uma lista
    for _ in range(qtde-1):#(quantidade que pediu para o usuário)
        fatoriais.append(next(gen)) # adiciona a lista os outros numeros da sequência
    print(f'Sequência de fatoriais iniciando em {prim}!')
    print(fatoriais)

    prim = int(input('\nDigite valor inicial para a próxima sequência: '))

print('\nFim do Programa')
