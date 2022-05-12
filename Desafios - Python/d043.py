print('-=' * 20)
print('Calculador de IMC')
print('-=' * 20)
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2
if (imc < 18.5):
    print('Você está com {:.2f} de IMC\nVocê está abaixo do peso!'.format(imc))
elif (imc <= 25):
    print('Você está com {:.2f} de IMC\nVocê está no peso ideal!'.format(imc))
elif (imc <= 30):
    print('Você está com {:.2f} de IMC\nVocê está no acima do peso!'.format(imc))
elif (imc <= 40):
    print('Você está com {:.2f} de IMC\nCUIDADO! Você está em indice de obesidade'.format(imc))
else:
    print('Você está com {:.2f} de IMC\nCUIDADO! Você está em indice de obesidade mórbida'.format(imc))