menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

>= """

saldo=0
limite=500
extrato=""
numero_saques=0
LIMITE_SAQUES=3
saque=0

while True:

    opcao=input(menu)

    if opcao=="d":
        deposito=float(input("Qual valor deseja depositar? R$"))
        print("Depósito de R${:.2f} efetuado com sucesso.".format(deposito))
        saldo+=deposito
        extrato+="Depósito de R${}\n".format(deposito)
    elif opcao=="s":
        saque=float(input("Digite o valor do saque."))
        if saque<=saldo and numero_saques<3 and saque>0 and saque<=500:
            saldo-=saque
            numero_saques+=1
            extrato+="Saque de R${}\n".format(saque)
            print("Saque de R${:.2f} efetuado com sucesso".format(saque))
        elif saque>saldo:
            print("Saldo insuficiente.Seu saldo é de R${}".format(saldo))
        elif numero_saques==3:
            print("Você atingiu o limite de 3 saques no dia, volte amanhã.")
        elif saque>500:
            print("O valor máximo permitido para saque é de R$500.00")
    elif opcao=="e":
        print(extrato)
        print("Seu saldo é de R${:.2f}".format(saldo))
    elif opcao=="q":
        break
    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")


