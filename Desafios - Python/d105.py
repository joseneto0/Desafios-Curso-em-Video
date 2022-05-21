def notas(*valores, sit=False):
    """
    Mostra o quantidade de valores, o menor valor, o maior valor, a média e a situação (caso seja verdadeira)
    :param *valores: quantidade indeterminada de valores
    :param sit: Mostra situação do aluno, caso verdadeira
    :param return: retorna um dicionario com as informações
    """
    dic = {}
    dic["total"] = len(valores)
    dic["maior"] = max(valores)
    dic["menor"] = min(valores)
    dic["média"] = sum(valores) / len(valores)
    if sit == True:
        if dic["média"] >= 7.00:
            dic["situação"] = 'BOA'
        elif dic["média"] > 5 and dic["média"] < 7:
            dic["situação"] = 'RAZOÁVEL'
        else:
            dic["situação"] = 'RUIM'
    return dic


#programa principal
resposta = notas(5.5, 9.5, 10, 6.5, 1.0, 2.0, sit=True)
print(resposta)