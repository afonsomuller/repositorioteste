contador_pessoas = 0
contador_pratao = 0
peso_total = 0
while True:
    peso = float(input('Digite o Peso do prato: [EM GRAMAS]\n'))
    if peso >= 800:
        contador_pratao += 1
    peso_total = peso_total + peso
    contador_pessoas += 1
    encerrar = str(input('Deseja Encerrar? [S/N]\n')).upper()
    if 'S' in encerrar:
        break
    elif 'N' in encerrar:
        print('Ok! Digite o Próximo valor!')
print(f'Hoje, {contador_pessoas} passaram pelo restaurante. \nO valor médio do peso foi de {(peso_total/contador_pessoas)/1000:.3f}.kgs \nTivemos {contador_pratao} de pratos acima de 800g')