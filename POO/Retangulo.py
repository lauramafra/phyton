class Retangulo:

    #Atributos
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    #Métodos
    #calcular_area()
    def calcular_area(self):
        return self.largura* self.altura

    #calcular_perimetro()
    def calcular_perimetro(self):
        return (self.largura*2)+(self.altura*2)


    #exebir_info()
    def exibir_info(self):
        print(f"O Retângulo possui {self.calcular_area()}cm² de área e {self.calcular_perimetro()}cm de perímetro total.")

    #Definindo objetos
r1 = Retangulo(largura=100, altura=200)
r2 = Retangulo(largura=200, altura=200)

#Chamando exibir info()
r1.exibir_info()
r2.exibir_info()