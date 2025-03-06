#EXERCICIO 55
maior=0
menor=0
for p in range(1,6):
    pesos=float(input('Qual o peso da {}° pessoa? '.format(p)))
    if p==1:
        maior=pesos
        menor=pesos
    else:
        if pesos> maior:
            maior= pesos
        if pesos<menor:
            menor=pesos
print('O maior peso foi {}kg\n e o menor peso foi de {}kg'.format(maior,menor))