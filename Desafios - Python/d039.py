import datetime
print('-=' * 20)
print('Alistamento Militar')
print('-=' * 20)
ano = int(input('Qual o ano do seu nascimento? '))
##esses 2 comandos de baixo pegam o ano atual
date = datetime.date.today()
anoatual = int(date.strftime('%Y'))
if (anoatual - ano < 18):
    print('Você ainda não precisa se alistar')
    print('Falta aproximadamente {} ano(s) para você se alistar'.format(18 - (anoatual - ano)))
    print('Ja está na hora de você se alistar!')
else:
    print('ATENÇÃO! VOCÊ PASSOU DO TEMPO LIMITE DE ALISTAMENTO')
    print('VOCÊ PASSOU {} ANO(S) DO PRAZO'.format((anoatual - ano) - 18))
    
