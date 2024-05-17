matriz_geral = []
matriz_media = []
cont_aluno = 1
while True:
    matriz_alunos = []
    matriz_alunos.append(f'Aluno {cont_aluno}')
    cont_aluno += 1
    matriz_geral.append(matriz_alunos[:])
    matriz_media.append(matriz_alunos[:])
    if cont_aluno == 5:
        break
for alunos in range(len(matriz_geral)):
    lista_notas = []
    for notas in range(1,4):
        lista_notas.append(float(input(f'Digite a {notas} nota do {alunos+1}º aluno: ')))
    matriz_geral[alunos].append(lista_notas[:])
print(matriz_geral)
for alunos in range(len(matriz_geral)):
    media = []
    soma = 0
    for notas in range(0,2):
        for notas2 in range(0,3):
            soma = soma + matriz_geral[alunos][1][notas2]
        media.append(media = soma / len(matriz_geral[alunos][1]))