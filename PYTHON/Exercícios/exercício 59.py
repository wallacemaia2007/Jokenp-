valor=0
from time import sleep
print('Bom dia,tudo bem?')
n1=int(input('Me passa o 1° valor: '))
n2 = int(input('Me passa o 2° valor: '))
print('Certo')
sleep(0.5)

while valor!=5:
    print('Oque você deseja fazer? ')
    sleep(0.5)
    valor=int(input('\033[31m[1]\033[mSomar\n'
                    '\033[31m[2]\033[mMultiplicar\n'
                    '\033[31m[3]\033[mQual o maior valor\n'
                    '\033[31m[4]\033[mpassar novos números\n'
                    '\033[31m[5]\033[mSair do programa\n'))
    if valor==1:
        print('A soma deles é {}'.format(n1+n2))
    elif valor==2:
        print('a multiplicação deles é {}'.format(n1*n2))
    elif valor==3:
        maior=n1
        if maior>n2:
            print('O maior valor é {}'.format(maior))
        else:
            print('O maior valor é {}'.format(n2))
    if valor == 4:
        n1 = int(input('Me passa o 1° valor: '))
        n2 = int(input('Me passa o 2° valor: '))
        print('Certo')
        sleep(0.5)
print('OK,desligando...')
