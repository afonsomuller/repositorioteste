lista_numeros = []
for num in range (6):
    lista_numeros.append(int(input(f'Digite o {num+1}º número sorteado:\n')))
print('Digite 6 números para comparar com a lista de números sorteados')
lista_compara = []
for num in range(6):
    numeros = int(input('Digite um número:\n'))
    lista_compara.append(numeros)
cont_acertos = 0
for contNumeros in range(len(lista_numeros)):
    for contCompara in range(len(lista_compara)):
        if lista_numeros[contNumeros] == lista_compara[contCompara]:
            cont_acertos += 1
if cont_acertos == 6:
    print('Parabéns, você ganhou na Mega Sena!')
elif cont_acertos == 5:
    print('Parabéns, você gnahou uma Quina!')
elif cont_acertos == 4:
    print('Parabéns, você ganhou uma Quadra!')
else:
    print('Você não ganhou nada, mas não desista, na próxima você pode ganhar!')
print(f'Os números sorteados foram: {lista_numeros}')


"""if lista_compara[num] == lista_numeros:
    cont_acertos += 1
    print(f'Você acertou o número {lista_compara[num]}')
else:
    print(f'Você errou o número {lista_compara[num]}')"""