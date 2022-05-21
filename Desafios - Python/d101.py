from datetime import date
def voto(ano):
    idade = date.today().year - ano
    if idade >= 18 and idade < 65:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO'
    elif idade >= 16 or idade >= 65:
        return f'Com {idade} anos: VOTO OPCIONAL'
    else:
        return f'Com {idade} anos: VOTO NEGADO'

print('-' * 20)
nascimento = int(input('Digite o ano do seu nascimento: '))
print(voto(nascimento))

#da para fazer assim tbm
'''if voto(nascimento) >= 18 and voto(nascimento) < 65:
    print(f'Com {voto(nascimento)} anos: VOTO OBRIGATÓRIO')
elif voto(nascimento) >= 16 or voto(nascimento) >= 65:
    print(f'Com {voto(nascimento)} anos: VOTO OPCIONAL')
else:
    print(f'Com {voto(nascimento)} anos: VOTO NEGADO')'''