print('_-'*40)
print('Sequencia de Fibanacci')
print('_-'*40)
contador=4
numero=int(input('Quantos termos voce quer? '))
n1 = 0
n2 = 1
n3=n1+n2
print(f'{n1} -> {n2} -> {n3} ',end='')
while contador<=numero:
    n4=n3+n2
    print(f'-> {n4} ',end='')
    n2=n3
    n3=n4
    contador+=1
print('\nAcabouu')
