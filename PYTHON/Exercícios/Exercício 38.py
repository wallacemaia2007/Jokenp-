#EXERCÍCIO 38
n1=str(input('Digite o 1° número:'))
n2=str(input('Digite o 2° número:'))
if n1>n2:
    print('O {} é o maior número'.format(n1))
    print('O {} é o menor número'.format(n2))
elif n2>n1:
    print('O {} é o maior número'.format(n2))
    print('O {} é o menor número'.format(n1))
elif n1==n2:
    print('Os números são iguais!!')
else:
    print('Escreve direito anta!')