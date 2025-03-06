#EXERCÍCIO 41
from datetime import date
ano=int(input('Bom dia!!Vamos ver em qual categoria você se encaixa?\nEm que ano você nasceu? '))
idade=date.today().year-ano
if idade<=9:
    print('Você tem {} anos e está na categoria MIRIM'.format(idade))
elif idade<=14:
    print('Você tem {} anos e está na categoria INFANTIL'.format(idade))
elif idade<=19:
    print('Você tem {} anos e está na categoria JUNIOR'.format(idade))
elif idade <= 25:
    print('Você tem {} anos e está na categoria SÊNIOR '.format(idade))
else:
    print('Você tem {} anos e está na categoria MASTER'.format(idade))