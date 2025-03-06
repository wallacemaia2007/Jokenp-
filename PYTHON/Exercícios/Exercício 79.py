valores=[]
resposta=''
while True:
    n=int(input('Digite um valor'))
    if n in valores!=True:
        print('Valor duplicado.... Não foi adicionado')
    else:
        print('Valor adicionado com sucesso!')
        valores.append(n)
    resposta=str(input('Você quer continuar?\n')).strip().upper()[0]
    if resposta=='N':
        break
print(sorted(valores))