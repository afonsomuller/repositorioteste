texto = str(input('Digite uma Frase: '))
vogal = 0
for letra in range(len(texto)):
    if texto[letra] == 'a' or texto[letra] == 'e' or texto[letra] == 'i' or texto[letra] == 'o' or texto[letra] == 'u':
        vogal += 1
print(vogal)
 
