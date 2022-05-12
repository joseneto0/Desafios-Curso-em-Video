print('-=' * 15)
print('Simulador de Empréstimo Bancário')
print('-=' * 15)
vcasa = float(input('Qual o valor da casa? R$ '))
vsalario = float(input('Qual o seu salário? R$ '))
vanos = int(input('Em quantos anos você quer pagar? '))
prestmax = vsalario / (30/100)
valorprest = vcasa / (vanos * 12)
if (vcasa / vanos > prestmax):
    print('Empréstimo Negado!')
    print('Você não consegue pagar uma prestação de R$ {:.2f} com seu salário atual'.format(valorprest))
else:
    print('Parabéns! Seu empréstimo foi aprovado!')
    print('A sua prestação vai ser de R$ {:.2f}'.format(valorprest))

