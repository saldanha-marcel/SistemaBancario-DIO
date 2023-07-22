# Projeto Versão desenvolvida Por Marcelo Saldanha

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


saldo = 0
limite = 500
extrato = []
numero_saques = 0 
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input('Qual valor deseja depositar? '))
        if valor > 0:
            saldo += valor
            extrato.append(f'Depósito: R$ {format(valor, ".2f")}')
            print('Deposito realizado com sucesso.')
        else:
            print('Valor informado é inválido, reveja o valor e refaça o depósito')
    elif opcao == 's':
        if numero_saques >= LIMITE_SAQUES: 
            print('Você excedeu o número de saque hoje, retorne amanhã')
        else:
            valor = float(input('Qual valor deseja sacar? '))
            if valor > limite:
                print(f'Valor para o Saque não disponivel, Você tem um limite de {limite} para saques')
            elif valor > saldo:
                print(f'Valor para o Saque não disponivel, seu saldo é R$ {format(saldo, ".2f")}')
            elif valor < 0:
                print(f'Valor informado é inválido, reveja o valor e refaça o saque')
            else:
                numero_saques += 1
                saldo = saldo - valor
                extrato.append(f'Saque: R$ {format(valor, ".2f")}')
                print('Saque realizado com sucesso.')
    elif opcao == 'e':
        if len(extrato) > 0:
            print('------------Extrato------------')
            for linha in extrato:
                print(linha)
            print('-------------------------------')
        else:
            print('Não foram realizadas movimentações.')
        print(f'Seu saldo atual é: R$ {format(saldo, ".2f")}')
    elif opcao == 'q':
        break

    else:
        print('Opção inválida, por favor selecione novamente a operação desejada.')