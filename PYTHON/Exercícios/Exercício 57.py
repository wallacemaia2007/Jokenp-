s=0
while s !='f' and s!= 'm':
    s = str(input('Qual seu sexo? ')).lower()
    if s !='f' and s!='m':
        print('digite denovo...')
if s =='m' or 'f':
    print('Anotado.')