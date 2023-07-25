menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""

saldo = 0 
LIMITE = 500
extrato = ''''''
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("Digite o valor do seu depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f'Depósito no valor de R$ {valor_deposito} \n'
        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == 's':
        if numero_saques < LIMITE_SAQUES:
            valor_saque = float(input("Digite o valor do seu saque: "))
            if valor_saque <= LIMITE and valor_saque <= saldo and valor_saque > 0:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f'Saque no valor de R$ {valor_saque} \n'
                print(f"""
                    Saque de R$ {valor_saque} realizado com sucesso!
                    Seu Saldo atual é R$ {saldo}.
                    """)
            elif valor_saque > saldo:
                print(f"""
                    Operação inválida, não será possível realizar o saque devido a falta de saldo.
                    Seu Saldo atual é R$ {saldo} e o saque que está tentando realizar é R$ {valor_saque}
                    """)
            elif valor_saque > LIMITE:
                print(f"""
                    Não será possível realizar o saque pois o valor excede o limite
                    de R$ {LIMITE} por Saque, tente novamente!!
                    """)
            else:
                print("Operação falhou! O valor informado é inválido.")        
        else:
            print(f"""
                Não será possível realizar o saque pois ja foram realizados 
                os {int(LIMITE_SAQUES)} saques diários permitidos.
                """)
    elif opcao == 'e':
        if len(extrato) == 0:
            print("Não Foram realizadas movimentações")
        else:    
            extrato += f'\nSeu Saldo atual é de R$ {saldo} \n'
            print(extrato)

    elif opcao == 'q':
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
