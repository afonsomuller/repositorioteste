senha = 1234
saldo = 0
passagem = 1
contador = 2
acesso = True
confirma_senha = 0

while acesso:
    usuario = int(input("Qual é o seu cartão de acesso?\n"
                        "Usuário - 1\n"
                        "Administrador - 2\n"
                        "Sair - 3\n"))
    if usuario == 1:
        menu1 = int(input("Seja bem-vindo, usuário!\n"
                          "O que deseja fazer?\n"
                          "Recarregar cartão - 1\n"
                          "Usar cartão - 2\n"
                          "Voltar - 3\n"))
        if menu1 == 1:
            saldo = float(input("Quantos créditos gostaria de recarregar?\n"))
            print(f"Novo saldo: {saldo:.2f} créditos\n")

        if menu1 == 2:
            if saldo < passagem:
                print("Você não possui saldo suficiente para essa transação\n")
            else:
                print(f"Novo saldo {saldo - passagem} créditos.\n")
                saldo = saldo - passagem

    if usuario == 2:
        confirma_senha = int(input("Por favor, digite sua senha.\n"))
        if confirma_senha != senha:
            while senha != confirma_senha:
                print("Senha incorreta.", contador, "tentativas restantes.")
                confirma_senha = int(input("Por favor, digite sua senha novamente.\n"))
                contador = contador - 1

            if contador == 0:
                print("Tentativas excedidas, tente novamente mais tarde.")
                break

        elif confirma_senha == senha:
            menu2 = int(input("Seja bem-vindo, administrador!\n"
                              "O que deseja fazer?\n"
                              "Visualizar créditos - 1\n"
                              "Atualizar valor da passagem - 2\n"
                              "Voltar - 3\n"))
            if menu2 == 1:
                print(f"Você possui {saldo} créditos.\n")

            if menu2 == 2:
                passagem = float(input("Qual o novo valor da passagem?\n"))

    if usuario == 3:
        acesso = False



"""while senha != confirma_senha:
    if contador > 0:
        print(f'Senha inválida! Você tem {contador} tentativas restantes')
        contador -= 1
        confirma_senha = int(input('Digite sua Senha:/n'))
    elif contador == 0:
        break"""