class Forma:
    def __init__(self, cor):
        self.cor = cor

    def calcular_area(self):
        return 0

    def exibir_info(self):
        print(f"Cor da forma: {self.cor} | Área: {self.calcular_area():.2f}")


class Circulo(Forma):
    def __init__(self, cor, raio):
        super().__init__(cor)
        self.raio = raio

    def calcular_area(self):
        return 3.14159 * (self.raio ** 2)


class Retangulo(Forma):
    def __init__(self, cor, largura, altura):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
        return self.largura * self.altura


class Triangulo(Forma):
    def __init__(self, cor, base, altura):
        super().__init__(cor)
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return (self.base * self.altura) / 2


# Instanciação
circulo = Circulo("Vermelho", 5)
retangulo = Retangulo("Azul", 10, 4)
triangulo = Triangulo("Verde", 6, 8)

print("--- Formas Geométricas ---")
circulo.exibir_info()
retangulo.exibir_info()
triangulo.exibir_info()