lista_numeros = []
cont = 0
for cont_numero in range(10):
    numero = int(input(f'Digite o {cont_numero+1}º valor:\n'))
    lista_numeros.append(numero)
localizador = int(input('Digite o número que deseja localizar:\n'))
for cont_localizador in range(len(lista_numeros)):
    if localizador != lista_numeros:
        print('Valor não encontrado')
        break
    elif localizador == lista_numeros[cont_localizador]:
        cont += 1
        print(f'O Número {localizador} foi localizado na {cont_localizador+1}º posição')
    else:
        print(f'O Número {localizador} não foi localizado na {cont_localizador+1}º posição')
print(f'O número {localizador} foi encontrado {cont} vezes durante a varredura')
