def validar_valores(numero, intervalo_inicial, intervalo_final):
    if numero <= intervalo_inicial or numero >= intervalo_final:
        return False
    else:
        return True
    
valor = int(input('Digite o valor: '))
prm_inicial = int(input('Digite o valor inicial: '))
prm_final = int(input('Digite o valor final: '))
verificacao = validar_valores(valor, prm_inicial, prm_final)
print(verificacao)