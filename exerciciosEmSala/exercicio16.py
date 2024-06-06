def calcularIMC(peso, altura):
    result = peso/(altura**2)
    return result

peso = float(input('Digite seu Peso: '))
altura = float(input('Digite sua Altura: '))
imc = calcularIMC(peso, altura)
print(f'{imc:.2f}')