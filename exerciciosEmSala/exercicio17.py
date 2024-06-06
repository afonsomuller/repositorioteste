def lerPalavras(frase):
    contador_palavras = 1
    for cont in range(len(frase_lida)):
        if frase_lida[cont] == ' ':
            contador_palavras += 1
    return contador_palavras

frase_lida = str(input('Digite sua frase:\n')).strip()

print(f'Foram Digitadas {lerPalavras(frase_lida)} Palavras')