print('==' * 5, 'LOJA DO ZEZIN', '==' * 5)
compra = float(input('Valor total da compra: R$ '))
print('Opções de pagamento:\n[1] - à vista (dinheiro/cheque) - 10% de desconto\n[2] - à vista (cartão) - 5% de desconto\n[3] - 2x no cartão\n[4] - 3x ou mais no cartão - 20% de juros.')
opcao = int(input('Qual sua opção de pagamento? [1, 2, 3, 4] '))
if opcao == 1:
    d10 = compra - (compra * 10/100)
    print('Você ganhou um desconto de 10%!\nSua compra ficará R$ {:.2f}'.format(d10))
elif opcao == 2:
    d5 = compra - (compra * 5/100)
    print('Você ganhou um desconto de 5%!\nSua compra ficará R$ {:.2f}'.format(d5))
elif opcao == 3:
    print('Você irá pagar 2 parcelas de R$ {:.2f}'.format(compra / 2))
elif opcao == 4:
    j20 = compra + (compra * 20/100)
    nparc = int(input('Em quantas parcelas: '))
    parc = j20 / nparc
    print('Você irá pagar com 20% de juros\nVocê pagará {} parcelas de R$ {:.2f}\nSua compra foi totalizada em R$ {:.2f}'.format(nparc, parc, j20))
else:
    print('OPÇÃO INVÁLIDA, TENTE NOVAMENTE')
  