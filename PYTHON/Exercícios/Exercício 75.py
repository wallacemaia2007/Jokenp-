from operator import index
lista=int(input('Digite um número ')),int(input('Digite outro número ')),int(input('mais um ')),int(input('só mais um '))
print('=-'*30)
print(f'Você digitou {lista}')
print('=-'*30)
print(f'O número 9 apareceu',lista.count(9),'vezes')
if lista.count(3)==0:
    print('O número 3 não foi digitado')
else:
    print(f'O número 3 apareceua primeira vez na posição {lista.index(3)+1}°')
print('Dentre os números digitados ',end='')
for pares in lista:
    if pares%2==0:
        print(pares,end=' ')
print('são pares')


