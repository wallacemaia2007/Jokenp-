#EXERCÍCIO 39
from datetime import date
ano=int(input('Bom dia! Em que ano você nasceu? '))
hj=date.today().year
idade=hj - ano
if idade>18:
    print('Putss, você está atrasado!! O certo era você se alistar com 18 anos, você está {} anos atrasado'.format(idade-18))
elif idade==18:
    print('Está na hora de se alistar ja!! Boa sorte')
elif idade<18:
    print('Tá cedo ainda... Falta {} anos para você se alistar!'.format(18-idade))