def gera_permuta(txt):
    if len(txt) <=1: 
        yield txt
    else:
        for i in range(len(txt)):
            atual = txt[i]
            resto = txt[:i] + txt[i+1:] # parte inicial + a parte final da frase
            for permuta in gera_permuta(resto):
                yield atual + permuta

texto = input("digite uma palavra")
for l in gera_permuta(texto):
    print(l)