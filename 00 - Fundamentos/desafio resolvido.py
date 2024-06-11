import pprint

saldo = 0
limite = 500
entrada, saida = [], []
num_saques, lim_saques = 0, 3
usuarios, contas = {}, {}
conta = 1

user_valido = ["Usuario válido", 12082004 , 28325243031, "Rua A", 123, "Jatiúca", "Maceió", "AL"]
cpf_repetido = ("CPF Repetido", 17092002, 28325243031, "Rua B", 987, "Ponta Verde", "Maceió", "AL")

def valor_invalido():
        print("\nO valor informado é INVÁLIDO.\n")

def depositar(valor, entrada, valor_invalido):
    global saldo
    if valor > 0:
        saldo += valor
        entrada.append(valor)
        print("\nDepósito feito com SUCESSO!!\n")
        print(f"Seu saldo após o depósito é de: R${saldo:2}\n")
        return saldo
    else:
        valor_invalido()

def sacar(valor, limite, saida, lim_saques, valor_invalido):
    global saldo
    global num_saques
    if valor <= saldo and valor <= limite and valor > 0:
        num_saques += 1
        if num_saques > lim_saques:
            print("\nNúmero de saques diário ULTRAPASSADO!\n")
        else:
            saida.append(valor)
            saldo -= valor
            print(f"\nSaque feito com SUCESSO!")
            print(f"Seu saldo após o saque é de: R${saldo:2}\n")
    elif valor > saldo:
        print("\nSaldo INSUFICIENTE!\n")
    elif valor > limite:
        print("\nValor acima do LIMITE!\n")
    else:
        valor_invalido()

def extrato(entrada, saida, saldo):
    print(f"""\n\n================ EXTRATO ================
Entradas:
    {"Não foram realizadas movimentações." if not entrada else entrada}
Saídas:
    {"Não foram realizadas movimentações." if not saida else saida}
    
Saldo: R$ {saldo:.2f}
==========================================\n\n""")

def criar_usuario(*, nome, data_nasc, cpf, rua, numero, bairro, cidade, estado):
    global usuarios
    user = {"nome":nome, "data de nascimento": data_nasc, "cpf": cpf, "contas":[], "endereço": {"logradouro": rua, "numero": numero, "bairro": bairro, "cidade": cidade + "/" + estado}}

    if usuarios.get(user["cpf"]):
        print("\nEsse CPF já está cadastrado!\n")
    else:
        usuarios[user["cpf"]] = user
        print("\nUsuário cadastrado com sucesso!\n")

def listar_usuarios():
    pprint.pprint(usuarios, width=60, depth=2, indent=4)
    print("\n")

def criar_conta(usuario, num_conta):
    global contas

    if not usuarios.get(usuario):
        print("\nNão é possível criar uma conta sem um usuário!\n")
        return

    if contas.get(num_conta):
        print("\nEssa conta já está cadastrada!\n")
    else:
        conta = {"num_conta": num_conta, "numero da agencia": "0001", "cpf do usuario": usuario}
        contas[num_conta] = conta
        print("\nConta cadastrada com sucesso!\n")

def listar_contas():
    pprint.pprint(contas, width=60, depth=2, indent=4)
    print("\n")

def listar_contas_cpf(usuarios):
    contas_dict = {cpf: usuario['contas'] for cpf, usuario in usuarios.items()}
    pprint.pprint(contas_dict, width=60, depth=2, indent=4)

while True:
    opcao = "inicial"
    print("""
    ================ BANCO ================
     [d] Depositar
     [s] Sacar
     [e] Extrato
    [nu] Novo usuário
    [nc] Nova conta
    [lu] Listar usuarios
    [lc] Listar contas
    [lp] Listar contas por CPF (ainda nÃo funciona)
     [q] Sair
""")
    opcao = input("=> ")

    if opcao == "inicial":
        continue

    elif opcao == "d":
        valor = float(input("\nInforme o valor do depósito: \n"))
        depositar(valor, entrada, valor_invalido)

    elif opcao == "s":
        valor = float(input("\nInforme o valor do saque: \n"))
        sacar(valor, limite, saida, lim_saques, valor_invalido)  
    
    elif opcao == "e":
        extrato(entrada, saida, saldo)
        saldo = saldo
    
    elif opcao == "nu":
        # nome = str(input("\nInforme o seu nome: \n"))
        # data = str(input("\nInforme a sua data de nascimento: \n"))
        # cpf = int(input("\nInforme o seu cpf: \n"))
        criar_usuario(nome="Usuario válido", data_nasc=12082004 , cpf=28325243031, rua="Rua A", numero=123, bairro="Jatiúca", cidade="Maceió", estado="AL")
        criar_usuario(nome="CPF Repetido", data_nasc=17092002, cpf=28325243032, rua="Rua B", numero=987, bairro="Ponta Verde", cidade="Maceió", estado="AL")
    
    elif opcao == "nc":
        criar_conta(28325243031, conta)
        if contas.get(conta):
            usuarios[28325243031]["contas"].append(conta)
            conta +=1
        else:
            continue
           
    elif opcao == "lu":
        listar_usuarios()
        
    elif opcao == "lc":
        listar_contas()

    # elif opcao == "lp":
    #     listar_contas_cpf(28325243031)
        
    elif opcao == "q":
        break

        #### NAO SEI PQ APARECE QUANDO FAZ O DEPOSITO
    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")