class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_info(self):
        print(f"Veículo: {self.marca} {self.modelo} ({self.ano})")

class Carro(Veiculo):
    def __init__(self, marca, modelo, ano, numero_portas):
        super().__init__(marca, modelo, ano)
        self.numero_portas = numero_portas

    def exibir_info(self):
        super().exibir_info()
        print(f"Número de portas: {self.numero_portas}")

class Moto(Veiculo):
    def __init__(self, marca, modelo, ano, cilindradas):
        super().__init__(marca, modelo, ano)
        self.cilindradas = cilindradas

    def exibir_info(self):
        super().exibir_info()
        print(f"Cilindradas: {self.cilindradas}cc")

# Instanciação
meu_carro = Carro("Toyota", "Corolla", 2022, 4)
minha_moto = Moto("Honda", "CB500", 2021, 500)

print("--- Informações do Carro ---")
meu_carro.exibir_info()
print("\n--- Informações da Moto ---")
minha_moto.exibir_info()