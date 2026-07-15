class Lampada:
    def __init__(self, marca):
        self.marca = marca

    def acender(self):
        print(f"Lâmpada {self.marca} acendendo...")

class LampadaIncandescente(Lampada):
    def acender(self):
        print(f"{self.marca}: Luz quente e amarelada acesa.")

class LampadaFluorescente(Lampada):
    def acender(self):
        print(f"{self.marca}: Luz branca e fria acesa.")

class LampadaLED(Lampada):
    def acender(self):
        print(f"{self.marca}: Luz LED de baixo consumo acesa.")

li1 = LampadaIncandescente("Philips")
li2 = LampadaIncandescente("Elgin")

lf = LampadaFluorescente("Osram")
lf2 = LampadaFluorescente("G-light")

ll1 = LampadaLED("Brilia")
ll2 = LampadaLED("Ourolux")

ligar_lampadas = [li1, li2, lf, lf2, ll1, ll2]

for Lampada in ligar_lampadas:
    Lampada.acender()
