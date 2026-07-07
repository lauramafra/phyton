class Calculadora:

    #Atributos
    def __init__(self):
        self.historico = []

    #Métodos
    #somar
    def somar(self, a, b):
        soma = a + b
        self.historico.append(f"{a} + {b} = {soma}")
        return soma
    #subtrair
    def subtrair(self, a, b):
        sub = a - b
        self.historico.append(f"{a} - {b} = {sub}")
        return sub

    #multiplicar
    def multiplicar(self, a, b):
        multiplicar = a * b
        self.historico.append(f"{a} * {b} = {multiplicar}")
        return multiplicar

    #dividir

    def dividir(self, a, b):
        if b == 0:
            print("Divisão impossível.")
            return None
        else:
            dividir = a / b
            self.historico.append(f"{a} / {b} = {dividir}")
            return dividir

    #exibir histórico
    def exibir_historico(self):
        if not self.historico:
            print("O histórico está vazio.")
        else:
            print("\n=== HISTÓRICO COMPLETO DE OPERAÇÕES ===")
            for operacao in self.historico:
                print(f"- {operacao}")
            print("=======================================\n")

# 1. Instanciar uma calculadora
calc = Calculadora()

# 2. Realizar pelo menos duas operações de cada tipo
calc.somar(10, 5)
calc.somar(22, 8)

calc.subtrair(50, 20)
calc.subtrair(100, 45)

calc.multiplicar(4, 5)
calc.multiplicar(7, 3)

calc.dividir(40, 2)
calc.dividir(9, 3)

# 3. Incluir uma tentativa de divisão por zero
calc.dividir(10, 0)

# 4. Exibir o histórico completo ao final
calc.exibir_historico()