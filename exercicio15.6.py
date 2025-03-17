def gera_media():
    total = qtde = 0
    while True:
        dado = (yield total / qtde if qtde > 0 else 0)
        if dado is not None:
            total += dado
            qtde += 1

gen = gera_media() # cria o gerador
next(gen) # inicializa o gerador
valor = input('Digite um valor (ou FIM para sair): ')

while valor.upper() != 'FIM':
    resultado = gen.send(float(valor)) # envia o valor
    print(f'média móvel atual = {resultado:.3f}\n')
    valor = input('Digite um valor (ou FIM para sair): ')

print(f'\nValor final da média = {resultado:.3f}')
print('\nFim do Programa')


