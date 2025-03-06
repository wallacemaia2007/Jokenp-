#EXERCÍCIO 42
n1=int(input('Digite o 1° lado '))
n2=int(input('Digite o 2° lado '))
n3=int(input('Digite o 3° lado '))
if n1<n2+n3 and n2<n1+n3  and n3<n1+n2:
    print('Os lados podem formar um triângulo')
    if n1==n2==n3:
        print('O triângulo é EQUILÁTERO!')
    elif n1==n2 or n1==n3 or n2==n3:
        print('O triângulo é ISÓCELES!')
    else:
        print('O triângulo é ESCALENO!')
else:
    print('Os lados NÂO podem formar um triângulo!')