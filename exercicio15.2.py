def gerador_fatorial():
    num, fat = 0, 1
    while True:
        yield num, fat
        num += 1
        fat *= num #nessa ordem
    
gen = gerador_fatorial()

n = int(input("inteiro"))
for _ in range (n): # não precisa de objeto de controle
    print (next(gen), end = ' ')