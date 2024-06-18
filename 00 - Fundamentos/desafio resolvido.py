import pprint

saldo = 0
limite = 500
entrada, saida = [], []
num_saques, lim_saques = 0, 3
usuarios, contas = {}, {}
conta = 1

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

def criar_usuario(*, nome, data_nasc, cpf, rua = "N/A", numero = 0, bairro = "N/A", cidade = "N/A", estado = "N/A"):
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
    [lp] Listar contas por CPF (ainda não funciona)
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
        nome = str(input("\nInforme o seu nome: \n"))
        data = str(input("\nInforme a sua data de nascimento: \n"))
        cpf = int(input("\nInforme o seu cpf: \n"))
        p_endereco = str(input("\nDeseja informar seu endereço? [S/N]"))
        
        if p_endereco == "s":
            rua = str(input("\nInforme a sua rua: \n"))
            numero = int(input("\nInforme o número: \n"))
            bairro = str(input("\nInforme o bairro: \n"))
            cidade = str(input("\nInforme a cidade: \n"))
            estado = str(input("\nInforme o estado: \n"))
            criar_usuario(nome=nome, data_nasc=data, cpf=cpf, rua=rua, numero=numero, bairro=bairro, cidade=cidade, estado=estado)
        elif p_endereco == "n":
            print("OK")
            criar_usuario(nome=nome, data_nasc=data, cpf=cpf)
        else: 
            valor_invalido()
            
    
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

    else:
        print("\nOperação inválida, por favor selecione novamente a operação desejada.")