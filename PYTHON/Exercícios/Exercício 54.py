#EXERCICIO 54
from datetime import date
maior=0
menor=0
for c in range(1,8):
    ano=int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade=date.today().year-ano
    if idade<18:
        menor+=1
    elif idade>=18:
        maior+=1
print('\033[32m{}\033[m pessoas são de maior\nE \033[32m{}\033[m são de menor'.format(maior,menor))