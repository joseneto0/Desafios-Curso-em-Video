from datetime import date
print('-=' * 20)
print('Confederação Nacional de Natação')
print('-=' * 20)
ano = int(input('Qual seu ano de nascimento? '))
anoatual = date.today().year
if (anoatual - ano <= 9):
    print('Você tem {} anos\nVocê está na categoria MIRIM'.format(ano))
elif (anoatual - ano <= 14):
    print('Você tem {} anos\nVocê está na categoria INFANTIL'.format(ano))
elif (anoatual - ano <= 19):
    print('Você tem {} anos\nVocê está na categoria JUNIOR'.format(ano))
elif (anoatual - ano <= 25):
    print('Você tem {} anos\nVocê está na categoria SÊNIOR'.format(ano))
else:
    print('Você tem {} anos\nVocê está na categoria MASTER'.format(ano))



