class Termostato:
    def __init__(self):
        self.__temperatura = 20

    #Getter
    def get_temperatura(self):
        return self.__temperatura

    #Setter
    def set_temperatura(self, valor):
        if   16<=  valor <= 30:
            self.__temperatura = valor
        else:
            print("Temperatura invalida!")

    #Método
    def exibir_status(self):
        print(f"Status do Termostato - Temperatura atual: {self.get_temperatura()} graus.")

#Instanciando um termostato
meu_termostato = Termostato()

meu_termostato.set_temperatura(25)
meu_termostato.set_temperatura(10)
meu_termostato.set_temperatura(35)
meu_termostato.set_temperatura(18)

print("-" * 40)
meu_termostato.exibir_status()