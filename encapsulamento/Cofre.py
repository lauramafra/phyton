class Cofre:
    def __init__(self, dono):
        self.dono = dono
        self.__valor = 0

    #Getter

    def get_valor(self):
        return self.__valor

    #Métodos
    def depositar(self, valor):
        if valor >0:
            self.__valor += valor
        else:
            print("Operação inválida: O valor do depósito deve ser positivo.")

    def retirar(self, valor):
        if valor <= self.__valor:
            self.__valor -= valor
        else:
            print(f"Operação inválida: Saldo insuficiente para retirar R$ {valor}.")

    def exibir_saldo(self):
        print(f"Dono do cofre: {self.dono}")
        print(f"Saldo atual: {self.get_valor()}")
        print("="*30)

#Cadastrando novos cofres
p1 = Cofre("Pedro")
p1.depositar(100)
p1.exibir_saldo()

p2 = Cofre("Laura")
p2.depositar(500)
p2.retirar(100)
p2.exibir_saldo()

p2.retirar(1000)
