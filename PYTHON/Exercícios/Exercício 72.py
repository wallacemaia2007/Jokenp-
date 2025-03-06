n=1
while True:
    n=int(input('Digite um núemro entre 0 a 20: '))
    if n>=0 and n<=20:
        break
números=('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','desesseis','desesete','desoito','desenove','vinte')
print('Você digitou o número ',números[n])


