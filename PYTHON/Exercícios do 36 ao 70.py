#EXERCÍCIO 36
#EXERCÍCIO 37
#n=int(input('Digite um número inteiro: '))
#info=int(input('Digite:\n1 para a converção em binário\n2 para converção em Octalz\n3 para converção para hexadecimal:\n'))
#if info==1:
#    print('{}'.format(bin(n)[2:]))
#elif info==2:
#    print('{}'.format(oct(n)[2:]))
#elif info==3:
#    print('{}'.format(hex(n)[2:]))
#else:
#    print('Aprende a ler primeiro animal')
from itertools import count


listan=[]
for c in range(0,5):
    if c ==0:
        listan.append(int(input('Digite um valor: ')))
        print(c)
        print(listan[c])

    else:
        print(c)
        x=int(input('Digite um valor: '))
        if listan[c]>listan[c-1]:
            listan.insert(listan.index((c-1)+1),x)
        if listan[c]<listan[c-1]:
            listan.insert(listan.index((c-1)-1),x)



















