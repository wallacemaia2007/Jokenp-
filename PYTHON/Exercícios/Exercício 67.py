while True:
    n=int(input('Qual tabuada você quer?\n'))
    if n<0:
        break
    print('_' * 20)
    for c in range(0,11):
        print(n ,'x', c,'=',n*c )
    print('_' * 20)
print('Acabamos por aqui')
