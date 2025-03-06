resposta='S'
media=maior=menor=c=z=0
while resposta in 'Ss':
    n=int(input('Digite um número: '))
    c+=1
    z+=n
    if c==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    resposta=str(input('Você quer continuar? '))
media=z/c
print('A média é de {}\nO maior número é {}\nE o menor número é {}'.format(media,maior,menor))