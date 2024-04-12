"""soma = 0
for cont in range(1,11):
    soma += cont
print(soma)
    
tabuada = int(input('Digite o valor que deseja calcular\n'))
for cont in range(1,11):
    resultado = tabuada * cont
    print(resultado)

numero = int(input('Digite um número: \n'))
while numero != 0:
    numero = int(input('Digite um número: \n'))

for count in range (0,10):
    numero = int(input('Digite um número: \n'))
    if numero < 0:
        print('Número inválido.')
    else:
        print(numero)


fatorial = 1
numero = int(input('Digite o valor a ser calculado: \n'))
if numero >= 1:
    contador = numero
    while contador > 1:
        fatorial *= contador
        contador -= 1
    print(fatorial)
else:
    if numero == 0:
        print(fatorial)
    else:
        print('Número Inválido')
        
numero = 0
for count in range(0,5):
    numero_digitado = int(input('Digite um valor: \n'))
    if numero_digitado > numero:
        numero = numero_digitado
    print(f'O maior número digitado até o momento é: {numero}')
print(f'O maior valor digitado foi {numero}')"""


massa = float(input('Digite a Massa do objeto: \n'))
tempo = 50
tempo_decorrido = 0
while massa > 0.5:
    tempo_decorrido += tempo
    massa /= 2
print(f'O tempo decorrido foi {tempo_decorrido} segundos')
print(f'A massa final é de {massa:.2f}')

"""lista = []
for cont in range(0,5):
    lista.append(int(input('Digite um número\n')))
    print(f'Você digitou os valores: {lista}')

print(f'O maior número digitado foi {max(lista)}')"""
