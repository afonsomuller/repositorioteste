def somar(valor_1, valor_2):
    soma = valor_1 + valor_2
    return soma

def subtrair(valor_1,  valor_2):
    subtracao = valor_1 - valor_2
    return subtracao

def multiplicar(valor_1, valor_2):
    multiplicacao = valor_1 * valor_2
    return multiplicacao

def dividir(valor_1, valor_2):
    if valor_1 != 0:
        divisao = valor_1 / valor_2
        return divisao
    else:
        return False


primeiro_numero = float(input('Digite o primeiro valor: '))
segundo_numero = float(input('Digite o segundo numero: '))
operador = int(input(f'Qual operação deseja fazer? \n'
                     '[1]: Soma \n'
                     '[2]: Multiplicação \n'
                     '[3]: Divisão \n'
                     '[4]: Subtração \n'))
if operador == 1:
    print(f'O Resultado da soma é: {somar(primeiro_numero, segundo_numero)}')
elif operador == 2:
    print(f'O Resultado da multiplicação é: {multiplicar(primeiro_numero, segundo_numero)}')
elif operador == 3:
    print(f'O Resultado da divisão é: {dividir(primeiro_numero, segundo_numero)}')
elif operador == 4:
    print(f'O Resultado da subtração é: {subtrair(primeiro_numero, segundo_numero)}')

