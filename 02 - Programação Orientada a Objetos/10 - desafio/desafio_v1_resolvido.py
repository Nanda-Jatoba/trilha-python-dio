from abc import ABC, abstractclassmethod, abstractproperty


class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.apppend(conta)

class PessoaFisica(Cliente):
    def __init__(self, nome, cpf, data_nasc):
        self._nome = nome
        self._cpf = cpf
        self._data_nasc = data_nasc


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, numero, cliente):
        return cls(numero, cliente)
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico
    

    def sacar(self, valor):
        saldo = self.saldo

        if valor > saldo:
            print("\nSaldo INSUFICIENTE!\n")
            return False
        elif valor <= 0:
            print("\nValor INVÁLIDO!\n")
            return False
        else: 
            saldo -= valor
            print("\nSaque feito com SUCESSO!\n")
            print(f"\nSaldo atual: R${saldo}\n")
            return True

    def depositar(self, valor):
        saldo = self._saldo

        if valor <= 0:
            print("\nValor INVÁLIDO!\n")
            return False
        else: 
            saldo += valor
            print("\nDepósito feito com SUCESSO!\n")
            print(f"\nSaldo atual: R${saldo}\n")
            return True

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite = 500, limite_saques = 3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__])

        if valor > self.limite:
            print("\nValor EXCEDIDO!\n")
            return False
        elif numero_saques >= self.limite_saques:
            print("\nLimite de saques EXCEDIDO!\n")
            return False
        else: 
            return super().sacar(valor)
        
    def __str__(self):
        return f"""\
            Agência:\t{self.agencia}
            C/C:\t\t{self.numero}
            Titular:\t{self.cliente.nome}
        """
    

class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor
            }
        )

class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethods
    def registrar(self,conta):
        pass


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        if conta.depositar(self.valor):
            conta.historico.adicionar_transacao(self)

class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    def registrar(self, conta):
        if conta.saca(self.valor):
            conta.historico.adicionar_transacao(self)