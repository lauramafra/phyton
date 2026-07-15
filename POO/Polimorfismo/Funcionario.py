class Funcionario:
    def __init__(self, nome):
        self.nome = nome

    def cumprimentar(self):
        print(f"Olá, meu nome é {self.nome}.")

class Recepcionista(Funcionario):
    def cumprimentar(self):
        print(f"Bem-vindo(a)! Meu nome é {self.nome}, posso ajudar?")

class Gerente(Funcionario):
    def cumprimentar(self):
        print(f"Olá! Sou {self.nome}, gerente desta unidade.")

class Tecnico(Funcionario):
    def cumprimentar(self):
        print(f"Oi, sou {self.nome}, do suporte técnico.")


# 1. Criação dos objetos
r1 = Recepcionista("Laura")
r2 = Recepcionista("Rafaela")

g1 = Gerente("João")
g2 = Gerente("Luis")

t1 = Tecnico("Tulio")
t2 = Tecnico("Pedro")

# 2. Guardando os objetos na lista
funcionarios = [r1, r2, g1, g2, t1, t2]

# 3. Loop para chamar o método cumprimentar() em todos
for funcionario in funcionarios:
    funcionario.cumprimentar()