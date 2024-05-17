lista_num = []
temp_list = []
for linha in range(0,2):
    for coluna in range(0,2):
        temp_list.append(int(input(f'Digite o {linha} {coluna} valor: ')))
    lista_num.append(temp_list[:])
    temp_list.clear()
print(lista_num)

for linha in range(0,2):
    soma = 0
    for coluna in range(0,2):
        soma = soma + lista_num[linha][coluna]
    print(soma)