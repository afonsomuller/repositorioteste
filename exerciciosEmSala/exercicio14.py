def calcular_comissao(valor_venda, porcentagem_comissao):
    comissao = valor_venda * porcentagem_comissao
    return comissao

venda = float(input('Digite o valor da venda: '))
porcentagem = int(input('Digite o valor da porcentagem da sua comissão: '))/100
print(f'O Valor da sua comissão deve ser {calcular_comissao(venda, porcentagem)}')
