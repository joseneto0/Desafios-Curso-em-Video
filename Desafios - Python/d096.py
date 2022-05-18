def area():
    area = largura * comprimento
    print(f'A área de um terreno {largura}x{comprimento} é de {area:.1f}m²')


#Programa principal
print('  Controle de Terrenos')
print('--' * 12)   
largura = float(input('LARGURA (m): '))
comprimento = float(input('COMPRIMENTO (m): '))
area()