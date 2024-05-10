produtos = []
quantidade_vendida = []
preco = []
for contador in range(0, 5):
    quantidade = int(input(f'Digite a quantidade vendida do {contador+1}º produto:\n'))
    quantidade_vendida.append(quantidade)
    valor = float(input(f'Digite o valor do {contador+1}º produto:\n'))
    preco.append(valor)
    produtos.append(f'Produto {contador+1}')
"""for contador in range(0, 5):
    if quantidade_vendida[contador] == 0:
        quantidade_vendida.pop(contador)
        preco.pop(contador)""" 
faturamento = 0
for contador in range(0,5):
    faturamento += quantidade_vendida[contador] * preco[contador]
print(f'O faturamento total foi de R${faturamento}')
print(produtos)
