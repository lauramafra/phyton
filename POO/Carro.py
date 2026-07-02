class Carro:

    #Atributos
    def __init__(self, marca, modelo,ano, km):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.km = 0

    #Métodos
    # #acelerar
    def acelerar(self, valor):
        self.km += valor
        return self.km

    #frear
    def frear(self, valor):
        self.km -= valor

        if self.km < 0:
         self.km = 0
        return self.km

    #exibir status
    def exibir_status(self):
        print(f"Carro: {self.marca} {self.modelo} ({self.ano}).")
        print(f"Velocidade atual: {self.km} km/h.")

    #Definindo objetos
c1= Carro("Fiat","Uno","2018",90)
c1.acelerar(60)
c1.exibir_status()

c2= Carro("Chevrolet","Onix","2020",50)
c2.acelerar(50)
c2.frear(20)
c2.frear(40)
c2.exibir_status()
