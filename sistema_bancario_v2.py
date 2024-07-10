class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco


class ContaCorrente:
    def __init__(self, agencia, numero_conta, usuario):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.usuario = usuario
        self.saldo = 0
        self.extrato = []
        self.numero_saques = 0


def criar_usuario(usuarios):
    nome = input("Digite o nome do usuário: ")
    data_nascimento = input("Digite a data de nascimento do usuário (DD/MM/YYYY): ")
    cpf = input("Digite o CPF do usuário: ")
    endereco = input("Digite o endereço do usuário (logradouro, número, bairro, cidade/UF): ")

    for usuario in usuarios:
        if usuario.cpf == cpf:
            print("CPF já cadastrado. Tente novamente.")
            return

    usuario = Usuario(nome, data_nascimento, cpf, endereco)
    usuarios.append(usuario)
    print("Usuário criado com sucesso!")


def criar_conta_corrente(contas, usuarios):
    cpf_usuario = input("Digite o CPF do usuário: ")
    for usuario in usuarios:
        if usuario.cpf == cpf_usuario:
            agencia = "0001"
            numero_conta = len(contas) + 1
            conta = ContaCorrente(agencia, numero_conta, usuario)
            contas.append(conta)
            print("Conta criada com sucesso!")
            return

    print("Usuário não encontrado. Tente novamente.")


def listar_contas(contas):
    for conta in contas:
        print(f"Agência: {conta.agencia}, Conta: {conta.numero_conta}, Usuário: {conta.usuario.nome}")


def depositar(conta, valor):
    if valor > 0:
        conta.saldo += valor
        conta.extrato.append(f"Depósito: R${valor:.2f}")
        print("Depósito realizado com sucesso!")
    else:
        print("Valor de depósito inválido. Tente novamente.")


def sacar(conta, valor, limite=500, limite_saques=3):
    if conta.numero_saques >= limite_saques:
        print("Você já realizou 3 saques diários. Tente novamente amanhã.")
        return

    if valor > 0 and valor <= limite:
        if conta.saldo >= valor:
            conta.saldo -= valor
            conta.extrato.append(f"Saque: R${valor:.2f}")
            conta.numero_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente. Não é possível realizar o saque.")
    else:
        print("Valor de saque inválido. Tente novamente.")


def ver_extrato(conta):
    print("Extrato da Conta:")
    for item in conta.extrato:
        print(item)
    print(f"Saldo atual: R${conta.saldo:.2f}")


# Inicialização de variáveis
usuarios = []
contas = []

while True:
    # Menu de opções
    print("\nSistema Bancário Básico")
    print("1. Criar Usuário")
    print("2. Criar Conta Corrente")
    print("3. Listar Contas")
    print("4. Operações Bancárias")
    print("5. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        # Criar Usuário
        criar_usuario(usuarios)

    elif opcao == "2":
        # Criar Conta Corrente
        criar_conta_corrente(contas, usuarios)

    elif opcao == "3":
        # Listar Contas
        listar_contas(contas)

    elif opcao == "4":
        # Operações Bancárias
        if not contas:
            print("Nenhuma conta cadastrada.")
            continue

        print("Selecione a conta:")
        for i, conta in enumerate(contas):
            print(f"{i+1}. Agência: {conta.agencia}, Conta: {conta.numero_conta}, Usuário: {conta.usuario.nome}")
        conta_selecionada = int(input("Digite o número da conta: ")) - 1

        if 0 <= conta_selecionada < len(contas):
            conta_atual = contas[conta_selecionada]

            while True:
                print("\n1. Depósito")
                print("2. Saque")
                print("3. Extrato")
                print("4. Voltar")

                opcao_banco = input("Escolha uma opção: ")

                if opcao_banco == "1":
                    valor = float(input("Digite o valor do depósito: "))
                    depositar(conta_atual, valor)

                elif opcao_banco == "2":
                    valor = float(input("Digite o valor do saque: "))
                    sacar(conta_atual, valor)

                elif opcao_banco == "3":
                    ver_extrato(conta_atual)

                elif opcao_banco == "4":
                    break

                else:
                    print("Opção inválida. Tente novamente.")
        else:
            print("Conta inválida. Tente novamente.")

    elif opcao == "5":
        print("Encerrando o sistema bancário. Até mais!")
        break

    else:
        print("Opção inválida. Tente novamente.")
