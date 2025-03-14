def filtragem(dados, vmin, vmax):
    for vals in dados:
        if vmin<= vals <= vmax:
            yield vals, vals*1.1

v = [11.9, 333, 98.7,55.5, 100]
min = int(input("valor minimo: "))
max = int(input("valor maximo: "))
teste = 1
gen = filtragem(v,min,max)
#while True:
#    if teste == 1:
#        print(next(gen))
#        teste = int(input("novo?"))
#    else:
#        break

for i in filtragem(v,min,max):
    print(i)

