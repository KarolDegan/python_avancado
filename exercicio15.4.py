import random
def gera_aleatorios(ini,fin):
    while True:
        yield random.randint(ini,fin)


qt = int(input("Quantidade de números: "))
inicial = int(input("Inicial: "))
final = int(input("Final: "))
gen = gera_aleatorios(inicial,final)

for _ in range(qt):
    print(next(gen), end = ' ')