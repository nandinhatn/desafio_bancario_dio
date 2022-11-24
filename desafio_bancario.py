menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""
saldo =0
limite =500
extrato =""
numero_saque =0
LIMITE_SAQUES =3

while True :
    opcao = input(menu)
    if opcao=='d':
        valor = int(input("Digite o valor para o depósito "))
        if valor <0:
            print("O valor digitado é inválido")
          
        else:
            saldo += valor
            print(f""" Depósito realizado com sucesso saldo atual R$ {saldo:.2f}.""")
            extrato += f"""Deposito Realizado R$ {valor:.2f} \n"""
            
    elif opcao =='s':
        valor_saque = int(input("Digite o valor para sacar: "))
        if valor_saque>saldo:
            print("Operação não permitida - SALDO INSUFICIENTE")
        elif  numero_saque>=3:
             print("Operação não permitida - SEU LIMITE DE SAQUES ESGOTOU")
        elif valor_saque> 500:
             print("Operação não permitida - O LIMITE DE SAQUE É DE R$ 500,00")
        elif valor_saque < 0:
            print("Valor inválido")
        else:
            saldo -= valor_saque
            print(f"""Saque  no valor de R$ {valor_saque:.2f} realizado com sucesso""")
            extrato += f""" Saque Realizado no valor de R$ {valor_saque:.2f} \n"""
            numero_saque += 1



    elif opcao == 'e':
        print("<<<<<<<<<<<<<<<<<<extrato<<<<<<<<<<<<<<<<<<")
        if extrato=="":
            print("Não foram realizadas movimentações")
        else:
            print(f"""{extrato}""")
            print(f"""Saldo : R$ {saldo:.2f}""")
            print("<<<<<<<<<<<<<<<<<<<<")
   
    elif opcao =='q':
         break
    else:
        print("opcao invalida , por favor selecione novamente a operação desejada")
