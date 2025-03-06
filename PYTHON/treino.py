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
    if valor==1327:
        print('Wowwwww')
        sleep(0.5)
        print('Esse número.......')
        sleep(1)
        print('É O NÚMERO DELAAAAAAAAA!!!! ')
        print('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHH')
        print('_______00000000000___________000000000000_________\n'
                '______00000000_____00000___000000_____0000000______\n'
                '____0000000_____________000______________00000_____\n'
                '___0000000_______________0_________________0000____\n'
                '__000000____________________________________0000___\n'
                '__00000_____________________________________ 0000__\n'
                '_00000______________________________________00000__\n'
                '_00000_____________________________________000000__\n'
                '__000000_________________________________0000000___\n'
                '___0000000______________________________0000000____\n'
                '_____000000____________________________000000______\n'
                '_______000000________________________000000________\n'
                '__________00000_____________________0000___________\n'
                '_____________0000_________________0000_____________\n'
                '_______________0000_____________000________________\n'
                '_________________000_________000___________________\n'
                '_________________ __000_____00_____________________\n'
                '______________________00__00_______________________\n')
        print('Fiquei feliz agora kkkkk obrigado :)')
        break
print('desligando...')


