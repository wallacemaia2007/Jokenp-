#EXERCICIO 1
#print('\033[35mOlá,Mundo!\033[m')
from idlelib.mainmenu import menudefs
#EXERCICIO 2
#nome=str(input('\033[35mQual seu nome? '))
#print('\033[35mPrazer em te conhecer \033[m {},\033[35m seu nome é lindo'.format(nome))

#EXERCICIO 3
#n1=int(input('\033[31m1° número:'))
#n2=int(input('2° número:'))
#print('\033[36m='*50)
#print('A soma entre {} e {} é {}'.format(n1,n2,n1+n2))
#print('\033[36m='*50)

#EXERCICIO 4
#algo=input('Digite algo: ')
#print(type(algo))
#print('é um número?\n {}'.format(algo.isnumeric()))
#print('é uma letra??\n {}'.format(algo.isalpha()))
#print('Está minúculo?\n {}'.format(algo.islower()))
#print('Está maiúsculo?\n {}'.format(algo.isupper()))

#EXERCICIO 5
#n=int(input('Escreva um número:'))
#print('Seu sucessor é {}\n Seu antecessor é {}'.format(n+1,n-1))

#EXERCICIO 6
#from math import sqrt
#n=int(input('Digite um número:'))
#print('Seu dobro é {} seu triplo {} e sua raiz é {}'.format(n*2,n*3,sqrt(n)))

#EXERCICIO 7
#n1=int(input('Digite sua 1° nota:'))
#n2=int(input('Digite sua 2° nota:'))
#print('a sua média será de {}'.format((n1+n2)/2))

#EXERCICIO 8
#d=int(input('Digite a medida a ser convertida:'))
#print('A medida {}m em cm e mm será respectivamente:\n {} e {}'.format(d,d*100,d*1000))

#EXERCICIO 9
#n= int(input('Escolha um numero: '))
#print('A tabuada do número {}:'.format(n))
#print('{} x {} = {}'.format(n,0,n*0))
#print('{} x {} = {}'.format(n,1,n*1))
#print('{} x {} = {}'.format(n,2,n*2))
#print('{} x {} = {}'.format(n,3,n*3))
#print('{} x {} = {}'.format(n,4,n*4))
#print('{} x {} = {}'.format(n,5,n*5))
#print('{} x {} = {}'.format(n,6,n*6))
#print('{} x {} = {}'.format(n,7,n*7))
#print('{} x {} = {}'.format(n,8,n*8))
#print('{} x {} = {}'.format(n,9,n*9))
#print('{} x {} = {}'.format(n,10,n*10))

#EXERCICIO 10
#n=int(input('Quanto de dinheiro você tem?'))
#print('Caso converta para dólares você terá cerca de {:.2f} dólares'.format(n/5.87))

#EXERCICIO 11
#l=int(input('Qual a largura da parede?'))
#c=int(input('Qual o comprimento da parede?'))
#print('A area total a ser pintada é {} e você gastará cerca de {} litros de tinta'.format(l*c,(l*c)/2))
#EXERCICIO 12
#n=int(input('Qual o valor do produto? '))
#print('O produto na promoção sairá por {} reais'.format(n-n*0.05))

#ERCICIO 13
#s=int(input('Qual o seu salário atual? '))
#print('Seu novo salário será de {:.2f} reais'.format(s*1.15))

#EXERCICIO 14
#t=int(input('Qual a temperatura em °C'))
#print('Convertendo para °F teremos que:\n {}°C === {}°F'.format(t,(t*1.8)+32))

#EXERCICIO 15
#d=int(input('Quantos dias o carro foi alugado? '))
#s=int(input('Qual foi a distância total percorrida com ele? '))
#print(('Você pagará um valor total de {} reais'.format((60*d)+(0.15*s))))

#EXERCICIO 16
#n=float(input('Digite un número: '))
#print('A parte inteira desse número é {}'.format(n//1))

#EXERCICIO 17

from math import pow,sqrt
from os.path import split
#ca=float(input('Valor do cateto adjacente: '))
#co=float(input('Valor do cateto oposto: '))
#print('O valor da hipotenusa será de {}'.format(sqrt(pow(ca,2)+(pow(co,2)))))

#EXERCICIO 18
#from math import sin,cos,tan,radians
#an=int(input('Digite um ângulo qualquer: '))
#ang=radians(an)
#print('Seu seno: {:.2f}\n'
 #     'cosseno: {:.2f}\n'
  #    'tangente:{:.2f}'.format(sin(ang),cos(ang),tan(ang)))

#EXERCICIO 19
#from random import choice
#a1=input('Nome de um aluno')
#a2=input('Nome de um aluno')
#a3=input('Nome de um aluno')
#a4=input('Nome de um aluno')
#lista=(a1,a2,a3,a4)
#print('O aluno sorteado é {}'.format(choice(lista)))

#EXERCICIO 20
from random import sample
#a1=input('Nome de um aluno ')
#a2=input('Nome de um aluno ')
#a3=input('Nome de um aluno ')
#a4=input('Nome de um aluno ')
#lista=(a1,a2,a3,a4)
#print('A ordem será {}'.format(sample(lista,4)))

#EXERCICIO 21
#mp3

#EXERCICIO 22
#n=input('Seu nome completo? ')
#div=n.split()
#print('{}\n{}\nSeu nome ao todo possui {} letras'.format(n.upper(),n.lower(),len(n)-n.count(' ')))
#print('Seu primeiro nome {} possui {} letras'.format(div[0],len(div[0])))

#EXERCICIO 23
#n=str(input('Digite um número: '))
#print('unidades:{}\ndezenas:{}\ncentenas:{}\nmilhar:{}'.format(n[3],n[2],n[1],n[0]))

#EXERCICIO 24
#n=str(input('Nome da cidade')).strip().lower()
#if n.find('santo')==0:
#    print('Sua cidade começa com santo')
#else:
#   print('Sua cidade NÃO começa com santo')
#EXERCICIO 25
#n=str(input('Seu nome completo: ')).lower().strip()
#if n.find('silva')==-1:
#    print('Seu nome NÃO possui com Silva')
#else:
#    print('Seu nome possui silva')
#EXERCICIO 26
#n=str(input('Digite uma frase: '))
#print(' A letra ''a'' aparece {} vezes na frase'.format(n.count('a')))
#print('Aparecendo a primeira vez na posição {} e a última vez {}'.format(n.find('a'),n.rfind('a')))

#EXERCICIO 27
#n=str(input('Qual o seu nome completo?'))
#div=n.split()
#print('Seu primeiro nome é {}\n E o último é {}'.format(div[0],div[-1]))

 #EXERCICIO 28
#from random import randint
#n=int(input('\033[31mESTOU PENSANDO EM UM NÚMERO......... VAMOS VER SE VOCÊ ADIVINHA HEHEHE\n QUAL NÚMERO EU PENSEI?\033[m\nEscolha um número de 0 à 5: '))
#sor=randint(0,5)
#if n==sor:
#    print('\033[32mQUE BOSTA EM.... VOCÊ ACERTOU O NÚMERO ERA {}......\nNA PRÓXIMA EU VENÇO!!'.format(sor))
#else:
#    print('\033[31mHAHAHAHHAHAHA PERDEU DENOVO OTÁRIO!!!\033[m\n não foi dessa vez... o número era {}'.format(sor))

#EXERCICIO 29
#n=int(input('Em que velocidade você estava? '))
#x=80
#if n>x:
#    print('\033[31mVocê foi multado! A multa será de \033[m{}\033[31m reais'.format((n-80)*7))
#else:
#    print('Deu sorte em... você não foi multado....')
#EXERCICIO 30
#n=int(input('Digite um número: '))
#if n%2==0:
#    print('Seu número é par')
#else:
#    print('Seu número é ímpar')
#EXERCICIO 31
#d=int(input('Bom dia! Qual foi a distância da viajem,em km? '))
#if d<200:
#    print('Certo, o valor a ser pago é de {} reais.'.format(d*0.50))
#else:
#    print('Certo, o valor a ser pago é de {} reais'.format(d*0.45))
#EXERCICIO 32
#a=int(input('Digite um ano! '))
#if a%4==0:
#    print('O ano {} é bissexto!!'.format(a))
#else:
#    print('O ano {} não é bissexto'.format(a))
#EXERCICIO 33
#n1=int(input('digite o 1° número: '))
#n2=int(input('digite o 2° número: '))
#n3=int(input('digite o 3° número: '))
#if n1<n2 and n1<n3:
#    menor=n1
#if n2<n1 and n2<n3:
#    menor=n2
#if n3<n1 and n3<n2:
#    menor=n3
#if n1>n2 and n1>n3:
#    maior=n1
#if n2>n1 and n2>n3:
#    maior=n2
#if n3>n1 and n3>n2:
#    maior=n3
#print('O maior número é {}\nE o menor é {}'.format(maior,menor))
#EXERCICIO 34
#s=int(input('Digite seu salário: '))
#if s<1250:
#    print('Seu aumento será de 15%, totalizando {} reais ao seu salário'.format(s*1.15))
#else:
#    print('Seu aumento será de 10%, totalizando {} reais ao seu salário'.format(s*1.1))
#EXERCICIO 35
#l1=int(input('Digite 1° lado: '))
#l2=int(input('Digite 2° lado: '))
#l3=int(input('Digite 3° lado: '))
#if l1>l2+l3 or l2>l1+l3 or l3>l1+l2:
#    print('Os lados \033[31mNÂO podem\033[m formar um triângulo!')
#else:
#    print('Os lados \033[32mpodem\033[m formar um triângulo!!')