#EXERCÍCIO 40
n1=float(input('Digite a sua 1° nota: '))
n2=float(input('Digite a sua 2° nota: '))
média=(n1+n2)/2
if média<5:
    print('Kakakka burro dms, REPROVADO!Sua média foi de {}'.format(média))
elif 5>=média<=6.9:
    print('Ta quase em, você está de RECUPERAÇÃO!!Sua média foi de {}'.format(média))
elif média>=7:
    print('Parabéns!!! você está APROVADO!!Sua média foi de {}'.format(média))