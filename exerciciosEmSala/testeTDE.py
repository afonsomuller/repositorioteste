"""resultados = [[],[],[]]
for jogos in range (0,3):
    placar = int(input(f'Quantos Gols o Brasil fez no {jogos+1} jogo?:\n'))
    resultados.(placar[0])
    placar = int(input(f'Qauntos Gols o adversário fez no {jogos+1} jogo?:\n'))
    resultados.append(placar[0])
print(resultados)"""

"""matriz = [[1,2,3],[4,5,6],[7,8,9]]
for linha, coluna in enumerate(matriz):
    print(f'Na linha {linha+1} temos os valores {coluna[0]}, {coluna[1]} e {coluna[2]}')

matrizInicDireta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for linha in range(0, 3):
    print("Linha", linha)
    for coluna in range(0, 3):
        print(matrizInicDireta[linha][coluna])"""
        
"""nLinhas = 3
nColunas = 2
matrizDinamica = [0] * nLinhas

for linha in range(nLinhas):
    matrizDinamica[linha] = [0] * nColunas

for linha, coluna in range(0,3):
    placar = int(input('Quantos Gols o Brasil fez no jogo?:\n'))
    matrizDinamica[linha][coluna] = placar
    placar = int(input(f'Qauntos Gols o adversário fez no jogo?:\n'))
    matrizDinamica[linha][coluna] = placar"""

lista_jogos1 = list()
lista_jogos2 = list()
lista_jogos3 = list()
lista_jogos4 = list()
lista_jogos5 = list()

for jogo in range(3):
    for apostador in range(5):
        placar = []
        print(f'Apostador {apostador+1}, digite os placares dos jogos:')
        placar.append(int(input(f'Quantos gols o Brasil fará no {jogo+1}º jogo?:\n')))
        placar.append(int(input(f'Quantos gols o Adversário fará no {jogo+1}º jogo?:\n')))
        if apostador == 0:
            lista_jogos1.append(placar[:])
        elif apostador == 1:
            lista_jogos2.append(placar[:])
        elif apostador == 2:
            lista_jogos3.append(placar[:])
        elif apostador == 3:
            lista_jogos4.append(placar[:])
        elif apostador == 4:
            lista_jogos5.append(placar[:])
print(lista_jogos1)
for resultado in range(5):
    print(f'O {resultado+1} apostador disse que o placar será:')
    if resultado == 0:
        print('Jogo 1: Brasil', lista_jogos1[0][0], 'x', lista_jogos1[0][1], 'Adversário')
        print('Jogo 2: Brasil', lista_jogos1[1][0], 'x', lista_jogos1[1][1], 'Adversário')
        print('Jogo 3: Brasil', lista_jogos1[2][0], 'x', lista_jogos1[2][1], 'Adversário')
    elif resultado == 1:
        print('Jogo 1: Brasil', lista_jogos2[0][0], 'x', lista_jogos2[0][1], 'Adversário')
        print('Jogo 2: Brasil', lista_jogos2[1][0], 'x', lista_jogos2[1][1], 'Adversário')
        print('Jogo 3: Brasil', lista_jogos2[2][0], 'x', lista_jogos2[2][1], 'Adversário')
    elif resultado == 2:
        print('Jogo 1: Brasil', lista_jogos3[0][0], 'x', lista_jogos3[0][1], 'Adversário')
        print('Jogo 2: Brasil', lista_jogos3[1][0], 'x', lista_jogos3[1][1], 'Adversário')
        print('Jogo 3: Brasil', lista_jogos3[2][0], 'x', lista_jogos3[2][1], 'Adversário')
    elif resultado == 3:
        print('Jogo 1: Brasil', lista_jogos4[0][0], 'x', lista_jogos4[0][1], 'Adversário')
        print('Jogo 2: Brasil', lista_jogos4[1][0], 'x', lista_jogos4[1][1], 'Adversário')
        print('Jogo 3: Brasil', lista_jogos4[2][0], 'x', lista_jogos4[2][1], 'Adversário')
    elif resultado == 4:
        print('Jogo 1: Brasil', lista_jogos5[0][0], 'x', lista_jogos5[0][1], 'Adversário')
        print('Jogo 2: Brasil', lista_jogos5[1][0], 'x', lista_jogos5[1][1], 'Adversário')
        print('Jogo 3: Brasil', lista_jogos5[2][0], 'x', lista_jogos5[2][1], 'Adversário')


"""for jogo in range(3):
    placar = []
    print('Apostador 1, digite os placares dos jogos:')
    placar.append(int(input(f'Quantos gols o Brasil fará no {jogo+1}º jogo?:\n')))
    placar.append(int(input(f'Quantos gols o Adversário fará no {jogo+1}º jogo?:\n')))
    lista_jogos1.append(placar)

for jogo in range(3):
    placar = []
    print('Apostador 2, digite os placares dos jogos:')
    placar.append(int(input(f'Quantos gols o Brasil fará no {jogo+1}º jogo?:\n')))
    placar.append(int(input(f'Quantos gols o Adversário fará no {jogo+1}º jogo?:\n')))
    lista_jogos2.append(placar)

for jogo in range(3):
    placar = []
    print('Apostador 3, digite os placares dos jogos:')
    placar.append(int(input(f'Quantos gols o Brasil fará no {jogo+1}º jogo?:\n')))
    placar.append(int(input(f'Quantos gols o Adversário fará no {jogo+1}º jogo?:\n')))
    lista_jogos3.append(placar)

for jogo in range(3):
    placar = []
    print('Apostador 4, digite os placares dos jogos:')
    placar.append(int(input(f'Quantos gols o Brasil fará no {jogo+1}º jogo?:\n')))
    placar.append(int(input(f'Quantos gols o Adversário fará no {jogo+1}º jogo?:\n')))
    lista_jogos4.append(placar)

for jogo in range(3):
    placar = []
    print('Apostador 5, digite os placares dos jogos:')
    placar.append(int(input(f'Quantos gols o Brasil fará no {jogo+1}º jogo?:\n')))
    placar.append(int(input(f'Quantos gols o Adversário fará no {jogo+1}º jogo?:\n')))
    lista_jogos5.append(placar)


print('O primeiro apostador disse que o placar será:')
print('Jogo 1: Brasil', lista_jogos1[0][0], 'x', lista_jogos1[0][1], 'Adversário')
print('Jogo 2: Brasil', lista_jogos1[1][0], 'x', lista_jogos1[1][1], 'Adversário')
print('Jogo 3: Brasil', lista_jogos1[2][0], 'x', lista_jogos1[2][1], 'Adversário')

print('O segundo apostador disse que o placar será:')
print('Jogo 1: Brasil', lista_jogos2[0][0], 'x', lista_jogos2[0][1], 'Adversário')
print('Jogo 2: Brasil', lista_jogos2[1][0], 'x', lista_jogos2[1][1], 'Adversário')
print('Jogo 3: Brasil', lista_jogos2[2][0], 'x', lista_jogos2[2][1], 'Adversário')

print('O terceiro apostador disse que o placar será:')
print('Jogo 1: Brasil', lista_jogos3[0][0], 'x', lista_jogos3[0][1], 'Adversário')
print('Jogo 2: Brasil', lista_jogos3[1][0], 'x', lista_jogos3[1][1], 'Adversário')
print('Jogo 3: Brasil', lista_jogos3[2][0], 'x', lista_jogos3[2][1], 'Adversário')

print('O quarto apostador disse que o placar será:')
print('Jogo 1: Brasil', lista_jogos4[0][0], 'x', lista_jogos4[0][1], 'Adversário')
print('Jogo 2: Brasil', lista_jogos4[1][0], 'x', lista_jogos4[1][1], 'Adversário')
print('Jogo 3: Brasil', lista_jogos4[2][0], 'x', lista_jogos4[2][1], 'Adversário')

print('O quinto apostador disse que o placar será:')
print('Jogo 1: Brasil', lista_jogos5[0][0], 'x', lista_jogos5[0][1], 'Adversário')
print('Jogo 2: Brasil', lista_jogos5[1][0], 'x', lista_jogos5[1][1], 'Adversário')
print('Jogo 3: Brasil', lista_jogos5[2][0], 'x', lista_jogos5[2][1], 'Adversário')"""

