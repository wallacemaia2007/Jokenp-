#EXERCICIO 56
soma=0
velho=0
nomevelho=''
f=0
for p in range(1,5):
    n=str(input('Nome da {}° pessoa:'.format(p))).strip()
    i=int(input('Idade: '))
    s=str(input('Sexo M/F:')).strip().upper()
    if p==1 and s=='M':
        velho=i
        nomevelho=n
    else:
       if i>velho:
            velho=i
            nomevelho=n
    if s=='F' and i<20:
        f+=1
    soma+=i
media=soma/4
print('A média das idade é de {}'.format(media))
print('O mais velho tem {} anos,e se chama {}'.format(velho,nomevelho))
print('O número de mulheres menores de 20 anos é {}'.format(f))