class contaBancaria:
    # Atributos
    def __init__(self, titular, numero, saldo=0):
        self.titular = titular
        self.numero = numero
        self.saldo = saldo

    # Métodos
    # depositar
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor de depósito inválido. O valor deve ser positivo.")

    # sacar
    def sacar(self, valor):
        if valor <= 0:
            print("Valor de saque inválido. O valor deve ser positivo.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        else:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado com sucesso.")

    # extrato
    def exibir_extrato(self):
        print("=" * 20)
        print(f"conta: {self.numero}") # Corrigido de numero_conta para numero
        print(f"titular: {self.titular}")