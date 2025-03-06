#EXERCÍCIO 43
peso=float(input('Digite seu peso (Kg): '))
altura=float(input('Digite sua altura: '))
imc=peso/(altura**2)
if imc<18.5:
    print('Seu IMC é {:.2f}\nVocê está abaixo do peso'.format(imc))
elif 18.5<imc<25:
    print('Seu IMC é {:.2f}\nVocê está no peso ideal! Seu IMC é muito bom!'.format(imc))
elif 25<imc<30:
    print('Seu IMC é {:.2f}\nVocê está sobrepeso!'.format(imc))
elif 30<imc<40:
    print('Seu IMC é {:.2f}\nVocê está com obesidade!! vá ao médico!'.format(imc))
else:
    print('Seu IMC é {:.2f}\nVocê está com OBESIDADE MÓRBIDA,vá ao médico URGENTEMENTE!!!!'.format(imc))