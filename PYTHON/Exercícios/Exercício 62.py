t1=int(input('Digite o 1° termo da P.A: '))
r=int(input('Digite a razão: '))
n=0
while n!=10:
    print(t1+r*n)
    n+=1
mais=int(input('Quer que mostre mais quantos termos?\n[0] para parar\n'))
if mais!=0:
    while 10+mais!=n:
        print(t1+r*n)
        n+=1
else:
    print('Acabou!')

