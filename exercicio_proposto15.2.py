def gera_primos2():
    v = 2
    while True:
        novo = (yield v)  # Retorna o primo atual e espera por um novo valor
        if novo is not None:
            if novo >= 2:
                v = novo  # Redefine o ponto inicial se válido
            else:
                print("O valor inicial não pode ser menor que 2. Continuando...")
                v = 2
        
        while True:
            if v == 2:
                yield v
                v = 3  # Próximo número a verificar
            elif v % 2 != 0:  # Números ímpares
                i = 3
                raiz = v ** 0.5
                while i <= raiz:
                    if v % i == 0:
                        break
                    i += 2
                else:
                    yield v  # Número primo encontrado
                v += 2  # Testa o próximo ímpar
            else:
                v += 1  # Garante que v seja ímpar, se não for 2

        


qt = int(input("quantidade de primos? "))
gen = gera_primos2()
next(gen)


prim = int(input('Numero inicial? '))

while True:
    r = gen.send(prim)
    print(r,end = ' ')
    for _ in range(qt-1):
        print(next(gen), end = ' ')

    prim = int(input("Próximo número (-1 para sair)"))

    if prim <0:
        break