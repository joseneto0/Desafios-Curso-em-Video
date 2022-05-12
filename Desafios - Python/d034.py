salario = float(input('Digite seu salário: '))
if salario > 1250.00:
    aumento1 = (salario * 10/100)
    print(f'Você vai receber um aumento de R$ {aumento1}, seu salário ficará R$ {aumento1 + salario}')
else:
    aumento2 = (salario * 15/100)
    print(f'Você vai receber um aumento de R$ {aumento2}, seu salário ficará R$ {aumento2 + salario}')

