#EXERCÍCIO 44
print('\033[32mBEM-VINDO!!ESTOU VENDENDO GOIABA!\nQUER COMPRAR UMA?')
valor=float(input('Como sou muito generoso me diga você, quanto você quer pagar na minha goiaba? $'))
print('Certo é negociável faço para você,qual vais ser a forma de pagamento?')
n=int(input('[ 1 ] à vista no dinheiro ou cheque( 10% de desconto)\n[ 2 ] à vista no cartão( 5% de desconto)\n[ 3 ] no cartão em até 2x( Sem juros )\n[ 4 ] 3x ou mais no cartão( juros de 20% sobre a goiaba)\n'))
if n==1:
    print('C tá doido vai pagar no dinheiro?? A goiaba vai custar ${}, fiz no precinho para você ;)'.format(valor-valor*0.1))
if n==2:
    print('Eita como mexe com internet em, consigo fazer por {} para você'.format(valor-valor*0.05))
if n==3 or n==4:
    vezes=int(input('Quantas vezes vc vai querer dividir mesmo? '))
    if vezes==2:
        print('Pobre é complicado em, mas fz oq divido em duas vezes de {} sem desconto.'.format(valor/2))
    elif vezes>=2:
        print('Kskkksks vc ta pior que eu em, mas vou ficar rico com essa goiaba hehhee, te cobro mais caro ela pelo juros da maquininha, sai por ${} no total dividindo em {} vezes consigo fazer ${} para vc'.format(1.2*valor,vezes,(1.2*valor/vezes)))