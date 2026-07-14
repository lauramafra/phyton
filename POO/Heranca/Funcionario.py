class Funcionario:
    def __init__(self, nome, salario_base):
        self.nome = nome
        self.salario_base = salario_base

    def calcular_salario(self):
        return self.salario_base

    def exibir_info(self):
        print(f"Nome: {self.nome} | Salário: {self.calcular_salario()}")


class Horista(Funcionario):
    def __init__(self, nome, salario_base, horas_trabalhadas, valor_hora):
        super().__init__(nome, salario_base)
        self.horas_trabalhadas = horas_trabalhadas
        self.valor_hora = valor_hora

    def calcular_salario(self):
        return self.horas_trabalhadas * self.valor_hora


class Mensalista(Funcionario):
    # Não precisa de construtor novo, herda tudo do pai
    pass


# Instanciação
func_horista = Horista("Carlos", 0, 160, 15.50)  # O salario_base pode ser 0 aqui pois será calculado
func_mensalista = Mensalista("Ana", 3200.00)

print("--- Funcionários ---")
func_horista.exibir_info()
func_mensalista.exibir_info()