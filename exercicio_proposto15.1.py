def gera_primos():
    yield 2
    v = 3
    while True:
        raiz = v**0.5
        i = 3
        while i <= raiz and v % i != 0:
            i+= 2
        if i > raiz:
            yield v
        
        v += 2

gen = gera_primos()

qt = int(input('Quantidade de primos: '))
primos = []
for _ in range(qt):
    primos.append(next(gen))

print(primos)
