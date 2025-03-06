contador18=homens=contadorm20=0
sexo=''
while True:
    print('\033[31m_'*30,'\033[m')
    print('Cadastrando Pessoas:')
    print('\033[31m_'*30,'\033[m')
    idade=int(input('Qual a idade?\n'))
    sexo = str(input('Qual o sexo? [H/M]\n')).strip().upper()[0]
    while sexo not in 'HM':
        sexo=str(input('Qual o sexo? [H/M]\n')).strip().upper()[0]
    print('\033[31m_'*30,'\033[m')
    if idade>18:
        contador18+=1
    if sexo=='H':
        homens+=1
    if sexo=='M' and idade<20:
        contadorm20+=1
    resposta=str(input('Você quer continuar? [S/N]\n')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('Você quer continuar? [S/N]\n')).strip().upper()[0]
    if resposta=='N':
        break
print(f'Dados digitados:')
print('\033[32m_' * 30, '\033[m')
print(f'O número total de pessoas maiores de 18 é {contador18}')
print(f'O número de Homens cadastrados é {homens}')
print(f'O número de mulheres maiores de 20 anos é {contadorm20}')

