class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.numero = numero
        self.titular = titular
        self.saldo = saldo
        self.extrato = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            print("Depósito realizado com sucesso!")
        else:
            print("Valor inválido para depósito.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def transferir(self, valor, conta_destino):
        if valor > 0 and valor <= self.saldo:
            self.saldo -= valor
            conta_destino.saldo += valor
            self.extrato.append(f"Transferência para {conta_destino.titular}: R$ {valor:.2f}")
            conta_destino.extrato.append(f"Transferência de {self.titular}: R$ {valor:.2f}")
            print(f"Transferência de R$ {valor:.2f} para {conta_destino.titular} realizada com sucesso!")
        else:
            print("Saldo insuficiente ou valor inválido.")

    def extrato_conta(self):
        print("Extrato da conta:")
        if self.extrato:
            for operacao in self.extrato:
                print(operacao)
        else:
            print("Sem movimentações.")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

class SistemaBancario:
    def __init__(self):
        self.contas = {}

    def abrir_conta(self):
        numero = input("Digite o número da conta: ")
        titular = input("Digite o nome do titular: ")
        self.contas[numero] = Conta(numero, titular)
        print(f"Conta {numero} criada para {titular} com sucesso!")

    def encerrar_conta(self):
        numero = input("Digite o número da conta a ser encerrada: ")
        if numero in self.contas:
            del self.contas[numero]
            print(f"Conta {numero} encerrada com sucesso!")
        else:
            print("Conta não encontrada.")

    def encontrar_conta(self):
        numero = input("Digite o número da conta: ")
        if numero in self.contas:
            return self.contas[numero]
        else:
            print("Conta não encontrada.")
            return None

    def menu(self):
        while True:
            print("\nMenu do Sistema Bancário:")
            print("1 - Abrir Conta")
            print("2 - Encerrar Conta")
            print("3 - Depositar")
            print("4 - Sacar")
            print("5 - Transferir")
            print("6 - Extrato")
            print("7 - Sair")

            opcao = input("Digite a opção desejada: ")

            if opcao == "1":
                self.abrir_conta()
            elif opcao == "2":
                self.encerrar_conta()
            elif opcao == "3":
                conta = self.encontrar_conta()
                if conta:
                    valor = float(input("Digite o valor do depósito: "))
                    conta.depositar(valor)
            elif opcao == "4":
                conta = self.encontrar_conta()
                if conta:
                    valor = float(input("Digite o valor do saque: "))
                    conta.sacar(valor)
            elif opcao == "5":
                conta_origem = self.encontrar_conta()
                if conta_origem:
                    numero_destino = input("Digite o número da conta destino:")
                    conta_destino = self.encontrar_conta()
                    if conta_destino:
                        valor = float(input("Digite o valor da transferência: "))
                        conta_origem.transferir(valor, conta_destino)
                    else:
                        print("Conta destino não encontrada.")
            elif opcao == "6":
                conta = self.encontrar_conta()
                if conta:
                    conta.extrato_conta()
            elif opcao == "7":
                print("Saindo do sistema...")
                break
            else:
                print("Opção inválida.")

sistema = SistemaBancario()
sistema.menu()
