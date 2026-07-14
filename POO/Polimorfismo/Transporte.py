class Transporte:
    def __init__(self, nome):
        self.nome = nome

    def viajar(self):
        return "Viajando..."

class Aviao(Transporte):
    def viajar(self):
            return "Voando..."

class Navio(Transporte):
    def viajar(self):
        return "Navegando..."

class Trem(Transporte):
    def viajar(self):
        return "Viajando de trem..."


def iniciar_viagem(transporte):
    transporte.viajar()

#Criando os objetos
aviao = Aviao("Boeing 737")
navio = Navio("Titanic")
trem = Trem("Expresso de Hogwarts")

#Criando a lista com os objetos (e não as classes)
lista_de_transportes = [aviao, navio, trem]

#Usando a função iniciar_viagem() em um loop para testar o polimorfismo
for veiculo in lista_de_transportes:
    iniciar_viagem(veiculo)