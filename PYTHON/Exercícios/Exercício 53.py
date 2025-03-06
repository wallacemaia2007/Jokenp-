#EXERCICIO 53
fr=str(input('DIgite uma frase: ')).strip().lower()
palavras=fr.split()
junto=''.join(palavras)
inverso=''
for c in range(len(junto)-1,-1,-1):
    inverso+=junto[c]
print('O inverso da frase {} é {}'.format(junto,inverso))
if junto==inverso:
    print('ou seja, a frase É UM PALÍNDROMO!!')
else:
    print('ou seJa, a frase NÃO É UM PALÍNDROMO!!')

