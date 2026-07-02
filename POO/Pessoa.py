class Pessoa:
    def __init__(self, nome, idade, cidade):
        self.nome = nome
        self.idade = idade
        self.cidade = cidade

#Métodos
#apresentar()

    def apresentar(self):
        print(f"Olá! Meu nome é {self.nome}, tenho {self.idade} anos e moro em {self.cidade}.")

p1 = Pessoa("Laura", 18, "Jaraguá do Sul")
p1.apresentar()

p2= Pessoa("Luis", "18", "Joinville")
p2.apresentar()

p3= Pessoa("Helena", "13", "Jaraguá do Sul")
p3.apresentar()