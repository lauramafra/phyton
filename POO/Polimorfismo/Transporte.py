class Transporte:
    def __init__(self, nome):
        self.nome = nome

    def viajar(self):
        print(f"{self.nome}: Viajando...")

class Aviao(Transporte):
    def viajar(self):
        print(f"{self.nome}: Voando...")

class Navio(Transporte):
    def viajar(self):
        print(f"{self.nome}: Navegando...")

class Trem(Transporte):
    def viajar(self):
        print(f"{self.nome}: Viajando de trem...")


def iniciar_viagem(transporte):
    transporte.viajar()

# 1. Criando objetos
meu_aviao = Aviao("Boeing 737")
meu_navio = Navio("Titanic")
meu_trem = Trem("Expresso de Hogwarts")

# 2. Criando a lista com os objetos
lista_de_transportes = [meu_aviao, meu_navio, meu_trem]

# 3. Usando a função iniciar_viagem() em um loop para testar o polimorfismo
for veiculo in lista_de_transportes:
    iniciar_viagem(veiculo)