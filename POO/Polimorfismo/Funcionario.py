class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        return print(f"Olá, meu nome é {self.nome}")

class Recepcionista(Funcionario):
    super().__init__("Recepcionista")
    def cumprimentar(self):
        return print(f"Bem-vindo (a)! Meu nome é {self.nome}, como posso ajudar?")

class Gerente(Funcionario):
    super().__init__("Gerente")
    def cumprimentar(self):
        return print(f"Olá! Sou {self.nome}, gerente desta unidade.")

class Tecnico(Funcionario):
    super().__init__("Técnico")
    def cumprimentar(self):
        return print(f"Oi, sou {self.nome}, do suporte técnico.")

r1 = Recepcionista("Laura")
r2= Recepcionista("Rafaela")

g