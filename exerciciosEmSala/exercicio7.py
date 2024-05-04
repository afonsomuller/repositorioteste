quantidade_vendida = []
preco = []
for contador in range(1, 101):
    quantidade = int(input(f'Digite a quantidade vendida do {contador}º produto:\n'))
    quantidade_vendida.append(quantidade)
    valor = float(input(f'Digite o valor do {contador}º produto:\n'))
    preco.append(valor)
for contador in range(1, 101):
    if quantidade_vendida[contador] == 0:
        quantidade_vendida.pop(contador)
        preco.pop(contador)
faturamento = 0
for contador in range(1,101):
    faturamento += quantidade_vendida[contador] * preco[contador]
print(f'O faturamento total foi de R${faturamento}')
