# 💰 DESAFIO DIO - SISTEMA BANCÁRIO (VERSÃO 2)
# Autor: Luana Silva (adaptação orientada por ChatGPT)
# Objetivo: modularizar o sistema com funções e incluir usuários e contas

# ==========================
# 🧩 VARIÁVEIS GLOBAIS
# ==========================

usuarios = []  # lista de dicionários com dados dos clientes
contas = []    # lista de dicionários com dados das contas
AGENCIA = "0001"


# ==========================
# 🏦 FUNÇÕES PRINCIPAIS
# ==========================

def depositar(saldo, valor, extrato, /):
    """Função de depósito (argumentos posicionais apenas)"""
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\n✅ Depósito realizado com sucesso!")
    else:
        print("\n⚠️  Operação falhou! Valor inválido para depósito.")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """Função de saque (argumentos nomeados apenas)"""
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n❌ Operação falhou! Saldo insuficiente.")
    elif excedeu_limite:
        print("\n❌ Operação falhou! Valor excede o limite de saque.")
    elif excedeu_saques:
        print("\n❌ Operação falhou! Número máximo de saques atingido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:    R$ {valor:.2f}\n"
        numero_saques += 1
        print("\n✅ Saque realizado com sucesso!")
    else:
        print("\n⚠️  Operação falhou! Valor inválido para saque.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    """Função de extrato (posição e nome misturados)"""
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("=========================================")


# ==========================
# 👤 FUNÇÕES DE USUÁRIO
# ==========================

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")

    usuario = filtrar_usuario(cpf, usuarios)
    if usuario:
        print("\n⚠️  Já existe usuário cadastrado com esse CPF!")
        return

    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
    endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla): ")

    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("\n✅ Usuário cadastrado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


# ==========================
# 🧾 FUNÇÕES DE CONTA
# ==========================

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n✅ Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n⚠️  Usuário não encontrado! Cadastro não realizado.")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
Agência: {conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}
"""
        print("=" * 30)
        print(linha)


# ==========================
# 🧠 LOOP PRINCIPAL
# ==========================

def main():
    LIMITE_SAQUES = 3
    limite = 500
    saldo = 0
    extrato = ""
    numero_saques = 0

    menu = """
================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[u] Criar usuário
[c] Criar conta
[l] Listar contas
[q] Sair
======================================
=> """

    while True:
        opcao = input(menu)

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, valor=valor, extrato=extrato,
                limite=limite, numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            criar_usuario(usuarios)

        elif opcao == "c":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "l":
            listar_contas(contas)

        elif opcao == "q":
            print("\n💼 Obrigado por utilizar o sistema bancário DIO!")
            break

        else:
            print("\n⚠️  Operação inválida! Tente novamente.")


# ==========================
# 🚀 EXECUÇÃO
# ==========================

if __name__ == "__main__":
    main()
