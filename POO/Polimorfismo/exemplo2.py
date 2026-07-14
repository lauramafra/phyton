import math


class Forma:
    def __init__(self, nome="Forma Geométrica"):
        self.nome = nome

    def calcular_area(self):
        return 0

    def descricao(self):
        return self.nome


class Circulo(Forma):
    def __init__(self, raio):
        super().__init__("Círculo")
        self.raio = raio

    def calcular_area(self):
        return math.pi * self.raio ** 2

    def descricao(self):
        return f"{self.nome}(raio = {self.raio})"


class Retangulo(Forma):
    def __init__(self, largura, altura):
        super().__init__("Retângulo")
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura

    def descricao(self):
        return f"{self.nome}({self.largura}, {self.altura})"

def exibir_area(forma):
    print(f"{forma.descricao()} - Area: {forma.calcular_area()}")

formas = [Circulo(5), Retangulo(3, 5), Circulo(2), Retangulo(8, 6)]

for forma in formas:
    exibir_area(forma)