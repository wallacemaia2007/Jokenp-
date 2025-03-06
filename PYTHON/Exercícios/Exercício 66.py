n=c=s=0
while True:
    n=int(input('Digite um número\n[999] para parar:\n '))
    if n==999:
        break
    s+=n
    c+=1
print(f'Você digitou {c} e a sua soma foi de {s}')