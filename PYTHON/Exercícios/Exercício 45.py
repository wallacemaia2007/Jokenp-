#EXERCÍCIO 45
from random import randint
from time import sleep
r='s'
contadorpc=contadorjogador=0
print('\033[31m-='*78)
print('\033[31m-='*20,'OLÁ JOGADOR...PRONTO PARA PERDER??','\033[31m-='*40)
print('\033[31m-='*23,'O JOGO DE HOJE É..','\033[31m-='*45)
print('\033[31m-='*25,'JOKEMPÔ!','\033[31m-='*48,)
sleep(1)
print('\033[31m-='*24,'VAI ENCARAR?','\033[31m-='*47)
print('\033[31m-='*78)
sleep(2)
print('\033[32m-='*78)
print('\033[32mSISTEMA: Olá jogador,caso queira jogar,siga as regras normais do jogo!')
while r!='n':
    print('\033[32m-='*78)
    v=int(input('Digite oque você irá jogar!\nDigite sua jogada!!\nPedra(0)\nPapel(1)\nTesoura(2)\n'))
    print('\033[31m-='*78)
    jogadas=('pedra','papel','tesoura')
    pc=randint(0,2)
    print('\033[31mVAMOS LÁ ENTÂO!!')
    print('\033[1;38mJO')
    sleep(1)
    print('KEM')
    sleep(1)
    print('PÔ!')
    print('\033[31m-='*78)
    if pc==0:
        if v==0:
            print('\033[31mEmpatamos, só dessa vez... \033[32mSISTEMA:Ambos jogaram {}'.format(jogadas[pc]))
        elif v==1:
            print('\033[31mAFF QUE DROGA... \033[32m\nSISTEMA:Você venceu!! Parabéns!! \n\033[32mEle jogou {}'.format(jogadas[pc]))
            contadorjogador+=1
        elif v==2:
            print('\033[31mHAHAHHAHAHAHA TENTA A SORTE DENOVO NOVATO!......\033[32m\nSISTEMA:Não foi dessa vez, quem sabe na próxima!\n\033[32mEle jogou {}'.format(jogadas[pc]))
            contadorpc+=1
        else:
            print('\033[32mSISTEMA:Comando inválido!')

    elif pc==1:
        if v==1:
            print('\033[31mEmpatamos, só dessa vez... \033[32mSISTEMA:Ambos jogaram {}'.format(jogadas[pc]))
        elif v==2:
            print('\033[31mAFF QUE DROGA... \033[32m\nSISTEMA:Você venceu!! Parabéns!! \n\033[32mEle jogou {}'.format(jogadas[pc]))
            contadorjogador+=1
        elif v==0:
            print('\033[31mHAHAHHAHAHAHA TENTA A SORTE DENOVO NOVATO!......\033[32m\nSISTEMA:Não foi dessa vez, quem sabe na próxima!\n\033[32mEle jogou {}'.format(jogadas[pc]))
            contadorpc+=1
        else:
            print('\033[32mSISTEMA:Comando inválido!')

    elif pc==2:
        if v==2:
            print('\033[31mEmpatamos, só dessa vez... \033[32mSISTEMA:Ambos jogaram {}'.format(jogadas[pc]))
        elif v==0:
            print('\033[31mAFF QUE DROGA... \033[32m\nSISTEMA:Você venceu!! Parabéns!! \n\033[32mEle jogou {}'.format(jogadas[pc]))
            contadorjogador+=1
        elif v==1:
            print('\033[31mHAHAHHAHAHAHA TENTA A SORTE DENOVO NOVATO!......\033[32m\nSISTEMA:Não foi dessa vez, quem sabe na próxima!\n\033[32mEle jogou {}'.format(jogadas[pc]))
            contadorpc+=1
        else:
            print('\033[32mSISTEMA:Comando inválido!')
    r=input('Deseja continuar?').lower()[0]
    while r not in 'sn':
        r=input('Deseja continuar?').lower()[0]
print('Fim de jogo.....')
sleep(1)
print('\033[32m-='*78)
print('PLACAR')
print(f'O Jogador fez {contadorjogador} pontos')
print(f'O computador fez {contadorpc} pontos')
print('\033[32m-='*78)
