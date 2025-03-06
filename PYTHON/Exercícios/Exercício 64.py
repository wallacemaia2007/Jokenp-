n=0
c=0
soma=0
while n!=999:
    n=int(input('Digite um número: '))
    if n!=999:
        c+=1
        soma+=n
    else:
        print('ok')
print('Você colocou {} números e sua soma foi de {}'.format(c,soma))
print('Fim')
