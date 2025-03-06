listan=[]
for c in range(0,5):
    x=int(input('Digite um valor: '))
    if c==0:#PRIMEIRO VALOR DIGITADO
        listan.append(x)
    elif x>listan[-1]:#CASO FOR O MAIOR VALOR
        listan.append(x)
    else:
        p=0#CONTADOR
        while p<len(listan):#ENQUANTO O CONTADOR BATER COM A QUANTIDADE DE TERMOS NA LISTA(ATÉ 5)
            if x<=listan[p]:#SE O X FOR MENOR DOQ O VALOR NA POSIÇÃO P INSIRA ELE ALI
                listan.insert(p,x)
                break
            p+=1
print(f'A sequência ficou:\n{listan}')