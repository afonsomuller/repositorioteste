notas = []
for cont_notas in range(5):
    nota = float(input(f'Digite a nota do {cont_notas+1}º aluno\n'))
    notas.append(nota)
soma = 0
for cont_notas in range(len(notas)):
    soma += notas[cont_notas]
media = soma/5
print(f'A média é {media:.2f}')
for cont_maior in range(len(notas)):
    if notas[cont_maior] > media:
        print(f'A nota do {cont_maior+1}º aluno, que foi {notas[cont_maior]} foi maior que a média da turma')
        