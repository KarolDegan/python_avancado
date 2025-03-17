def gera_primos2():
    yield 2
    v = 3
    while True:
        i = 3
        raiz = v**0.5
        while i <= raiz and v % i !=0:
            i+=2
        if i> raiz:
            valor = (yield v)
            if valor is not None:
                v = valor
                if valor < 2:
                    raise ValueError(f'Esperado valor maior ou igual a 2, passado {valor}')

        v +=2


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