menu = """
----- Sistema Bancário ------
|                           |
| [d] Depositar             |
| [s] Sacar                 |
| [e] Extrato               |
| [q] Sair                  |
-----------------------------
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
numero_movimentacao = 0

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = int(input("Insira o valor do depósito: "))

        if valor > 0:
            saldo += valor
            numero_movimentacao += 1
            extrato += f"{numero_movimentacao} - Operação de depósito: R$ {valor:.2f}\n---------------------------------------\n"
            print("Depósito realizado!")
        else:
            print("Insira um valor válido!")

    elif opcao == "s":
        if numero_saques < 3:
            valor = int(input("Insira o valor do saque: "))

            if valor > saldo:
                print("Não foi possível fazer o saque por falta de saldo.")
            else :
                if valor > 0 and valor <= 500:
                    saldo -= valor
                    numero_movimentacao += 1
                    extrato += f"{numero_movimentacao} - Operação de saque: R$ {valor:.2f}\n---------------------------------------\n"
                    numero_saques += 1
                    print("Saque realizado!")
                else:
                    print("O valor máximo do saque é R$ 500,00.")
        else:
            print("Você não pode realizar mais de 3 saques por dia!")

    elif opcao == "e":
        if extrato == "":
            print("Não foram realizadas movimentações.")
        else:
            print(extrato)
            print(f"Saldo atual: R$ {saldo:.2f}")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")