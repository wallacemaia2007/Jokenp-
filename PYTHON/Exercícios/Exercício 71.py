cinquenta=vinte=dez=um=0
valor=int(input('Digite um valor: '))
while valor-50>=0:
    valor-=50
    cinquenta+=1
while valor-20>=0:
    valor-=20
    vinte+=1
while valor-10>=0:
    valor-=10
    dez+=1
while valor-1>=0:
    valor-=1
    um+=1
print(f'Você receberá')
if cinquenta>0:
    print(f'{cinquenta} notas de 50 reias')
if vinte > 0:
    print(f'{vinte} notas de 20 reais')
if dez > 0:
    print(f'{dez} notas de 10 reais')
if um > 0:
    print(f'{um} notas de 1 real')
