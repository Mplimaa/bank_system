def menu():
    return """
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[q] Sair
=> """


def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! Valor inválido.")

    return saldo, extrato
    

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Saldo insuficiente.")

    elif excedeu_limite:
        print("Valor excede o limite.")

    elif excedeu_saques:
        print("Número máximo de saques atingido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Valor inválido.")

    return saldo, extrato, numero_saques


def mostrar_extrato(saldo, extrato):
    print("\n========== EXTRATO ==========")
    print("Nenhuma movimentação." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("=============================")

    if not usuarios:
        print("Nenhum usuário cadastrado.")
    else:
        for usuario in usuarios:
            print(f"""Nome: {usuario['nome']} 
CPF: {usuario['cpf']} 
Data de nascimento: {usuario['data_nascimento']}
Endereço: {usuario['endereco']} ------------------------------""")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("Usuário já existe.")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço: ")

    usuarios.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []

while True:

    opcao = input(menu())

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
            # print("DEBUG ENTROU NO DEPÓSITO")
            # saldo, extrato = depositar(saldo, extrato)
            # print("DEBUG EXTRATO:", repr(extrato))


    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            valor=valor,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            limite_saques=LIMITE_SAQUES
        )

    elif opcao == "e":
        mostrar_extrato(saldo, extrato)

    elif opcao == "u":
        criar_usuario(usuarios)

    elif opcao == "q":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida.")
