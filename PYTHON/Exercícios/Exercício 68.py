from random import randint, choice, shuffle, sample
par='P'
impar='I'
soma=contador=0
print('=-'*40)
print('VAMOS JOGAR PAR OU ÍMPAR?')
print('=-'*40)
while True:
    valor=int(input('Digite um número/:\n'))
    valorpc=randint(0,10)
    escolha=str(input('Você quer par ou impar? [P/I]')).strip().upper()[0]
    if escolha==par:
        escolhapc=impar
    elif escolha==impar:
        escolhapc=par
    else:
        print('Digite par ou ímpar.')
        break
    soma=valor+valorpc
    print(f'O computador jogou {valorpc}')
    if soma%2==0:
        print('Soma é par')
        if escolhapc==par:
            print('O computador ganhou')
            break
        else:
            print('Você ganohu!')
            contador+=1
            print('Vamos de novo?')
    else:
        print('Soma é impar')
        if escolhapc==impar:
            print('O computador ganhou!')
            break
        else:
            print('Você ganhou!!')
            contador+=1
            print('Vamos de novo?')
print(f'Você ganhou {contador} seguidas!!!')



