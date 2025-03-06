#EXERCICIO 52
n=int(input('Escolha um núemro: '))
t=0
for c in range(1,n+1):
    if n% c ==0:
        t+=1
if t==2:
    print('Ele é primo')
else:
    print('Ele não é primo')