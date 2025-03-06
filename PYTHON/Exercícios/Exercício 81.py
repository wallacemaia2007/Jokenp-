c=0
c2=0
r=''
números=[]
while True:
    números.append(int(input('Digite um valor:\n')))
    c+=1
    if 5 in números:
        c2+=1
    r=str(input('Quer continuar? [S/N]\n')).strip().upper()[0]
    if r=='N':
        break
ordenada=números.sort(reverse=True)
print(f'Foram digitados {c} números')
print(f'Os números em ordem decrecente ficam:\n{ordenada}')
if 5 in números:
    print(f'O número 5 apareceu {c2} vezes')
else:
    print('O número 5 não apareceu')