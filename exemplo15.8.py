def fg(): #gerador tanto de numeros pares quanto de impares
    resto = 0
    num = 2
    while True:
        if num % 2 == resto:
            print("primeiro: " + str(num))
            dado = (yield num) # O gerador yield retorna o valor de num para o chamador. Isso faz com que a execução da função fg() seja suspensa até que um valor seja enviado de volta pelo método send().
                # com o send ele volta aqui
            print("segundo: " + str(num))
            print("dado: " + str(dado))
            if dado is not None:
                print(num)
                if dado not in (0, 1):
                    raise ValueError(f'Esperado 0 ou 1 - passado {dado}')
                resto = dado # troca o valor de resto
                num = 0 # reseta o valor de num
                print("terceiro: " + str(num))
        num += 1

gen = fg()
print('Gera 5 pares')
for i in range(5):
    print(next(gen)) # como o next não envia nada o valor do num permanece 2 que é retornado(yield), dado = none

print('\nGera 5 ímpares')
ret = gen.send(2) # este método retorna o 1º valor da sequência que é 1 após o num ser zerado e novamente acrescido de +=1
print(ret) # imprime o 1 aqui
for i in range(4): # então precisamos gerar o próximos 4
    print("impressão: " + str(next(gen)))
    # na primeira entrada do iterativo o dado fica como none, então não entra is not None