soma=maisq1000=maisbarato=c=0
while True:
    nome=str(input('Nome do produto: '))
    preço=int(input('Qual o preço do produto? '))
    soma+=preço
    resposta=str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if preço>1000:
        maisq1000+=1
    if c==0:
        maisbarato = preço
        c+=1
        n = nome
    elif c!=0:
        if preço<maisbarato:
            maisbarato=preço
            n=nome
    if resposta in 'N':
        break
print('\033[32m=-'*20,'\033[m')
print('fechando a conta:   ')
print('\033[32m=-'*20,'\033[m')
print(f'O valor total foi de \033[32m{soma}\033[m')
print(f'No su carrinho tem \033[32m{maisq1000}\033[m produtos mais que 1000,00 reias')
print(f'O produto mais barato no seu carrinho é o \033[32m{n}\033[m de \033[32m{maisbarato}\033[m reais')


