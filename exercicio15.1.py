def gerador_primos():
    yield 2
    v = 3
    while True:
        raiz = v ** 0.5
        i = 3
        print("1")
        print(v,i,raiz)
        while i <= raiz and v % i != 0:
            i += 2
            print("2")
            print(v,i,raiz)
        if i > raiz:
            print("3")
            print(v,i,raiz)
            yield v
        print("4")
        print(v,i,raiz)
        v += 2

gen = gerador_primos()


while True:
    teste = int(input("novo primo? "))
    if teste == 1:
        print(next(gen))
    else:
        break