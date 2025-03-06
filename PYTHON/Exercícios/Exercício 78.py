listan=[]
maior=menor=0
for v in range(0,5):
    listan.append(int(input(f'Digite um valor para a posição {v}: ')))
    if v==0:
        maior=menor=listan[v]
    else:
        if listan[v]>maior:
            maior=listan[v]
        elif listan[v]<menor:
            menor=listan[v]
print(f'Você digitou os números {listan}')
print(f'O maior valor é {maior} na posição',end='')
for p,v in enumerate(listan):
    if v == maior:
        print(f'...{p}',end='')
print(f'\nE o menor valor é {menor} na posição ',end='')
for p,v in enumerate(listan):
    if v == menor:
        print(f'...{p}',end='')