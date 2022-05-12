v1 = float(input('Primeira nota: '))
v2 = float(input('Segunda nota: '))
media = (v1 + v2) / 2
if media < 5.0:
    print('Você ficou com {:.2f} de média.'.format(media))
    print('Sua média ficou abaixo de 5.0, você está REPROVADO')
elif media > 5.0 and media < 7:
    print('Você ficou com {:.2f} de média.'.format(media))
    print('Você terá que fazer a recuperação')
else:
    print('Você ficou com {:.2f} de média.'.format(media))
    print('Parabéns! Você foi aprovado!')