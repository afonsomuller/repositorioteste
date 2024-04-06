usuario = 1
creditos_cartao = 0.0
valor_passagem = 6.0
senha = 1234
contador = 2
acesso = True
if acesso:
    while acesso:
        usuario = int(input('Qual seu usuário?\n'
                            'Administrador - 1\n'
                            'Usuário - 2\n'
                            'Sair - 3\n'))
        if usuario < 1 or usuario > 3:
            print('Opção inválida. Tente novamente.')
        if usuario == 1:
            confirma_senha = int(input("Por favor, digite sua senha.\n"))
            while senha != confirma_senha:
                if contador > 0:
                    print(f'Senha incorreta. {contador} tentativas restantes.')
                    confirma_senha = int(input("Por favor, digite sua senha novamente.\n"))
                    if senha == confirma_senha:
                        contador = 2
                        pass
                    contador = contador - 1
                elif contador == 0:
                    break
            if contador == 0:
                print("Tentativas excedidas, tente novamente mais tarde.")
                break
            elif senha == confirma_senha:
                contador = 2
                opcoes = int(input('Bem vindo Administrador!\n'
                                    'O que você deseja fazer?\n'
                                    'Visualizar créditos do cartão - 1\n'
                                    'Alterar Valor da passagem - 2\n'
                                    'Sair - 3\n'))
            if opcoes == 1:
                print(f'O Usuário tem {creditos_cartao} créditos restantes.')
            elif opcoes == 2:
                valor_passagem = float(input('Qual valor da passagem você deseja definir? \n'))
                print(f'O Valor da passagem foi alterado para: R${valor_passagem:.2f}')