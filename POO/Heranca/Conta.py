class Conta:
    def __init__(self, titular, saldo=0.0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de {valor} efetuado. Saldo atual: {self.saldo}")

    def exibir_saldo(self):
        print(f"Saldo do(a) {self.titular}: {self.saldo}")

class ContaPoupanca(Conta):
    def __init__(self, titular, saldo, taxa_rendimento):
        super().__init__(titular, saldo)
        self.taxa_rendimento = taxa_rendimento

    def render(self):
        self.saldo = self.saldo * (1 + self.taxa_rendimento)
        print(f"Rendimento aplicado. Novo saldo: {self.saldo:.2f}")

class ContaCorrente(Conta):
    def __init__(self, titular, saldo, limite):
        super().__init__(titular, saldo)
        self.limite = limite

    def depositar(self, valor):
        if valor <= 0:
            print("Erro: Não é possível depositar valores negativos ou nulos.")
        else:
            super().depositar(valor)

    def sacar(self, valor):
        if valor <= (self.saldo + self.limite):
            self.saldo -= valor
            print(f"Saque de {valor} efetuado com sucesso. Saldo atual: {self.saldo}")
        else:
            print("Erro: Saldo e limite insuficientes para este saque.")

# Instanciação
poupanca = ContaPoupanca("João", 1000, 0.05)
corrente = ContaCorrente("Maria", 500, 200)

print("--- Conta Poupança ---")
poupanca.exibir_saldo()
poupanca.render()

print("\n--- Conta Corrente ---")
corrente.exibir_saldo()
corrente.depositar(-50)
corrente.depositar(100)
corrente.sacar(700) # Usando o limite
corrente.exibir_saldo()