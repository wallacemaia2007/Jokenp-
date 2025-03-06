from random import randint
x=0
n=int(input('Pensei em um número de 0 à 10...Qual número eu pensei?'))
pc=randint(0,10)
while n!=pc:
    n=int(input('Não,tenta denovo:\n '))
    x+=1
print('Acertou miserávi, mas você tentou {} vezes'.format(x))