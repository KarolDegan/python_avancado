def qt_fatorial():
    num, fat = 0, 1
    while True:
        i = (yield num, fat) 
        num += 1
        fat *= num 
        if i is not None:
            if i < 0:
                raise ValueError(f'Não esperados valores menores do que zero!')
            num = i 
            fat = 1
            for a in range(1, num+1):
                fat *= a

qtde = int(input('Digite a quantidade de fatoriais: '))
gen = qt_fatorial()
next(gen)

prim = int(input('\nDigite valor inicial para a próxima sequência: '))

while True:
    r = gen.send(prim)
    fatoriais = [r]
    for _ in range(qtde-1):
        fatoriais.append(next(gen)) 
    print(f'Sequência de fatoriais iniciando em {prim}!')
    print(fatoriais)

    prim = int(input('\nDigite valor inicial para a próxima sequência: '))

print('\nFim do Programa')
