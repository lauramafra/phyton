class Animal:
    def emitir_som(self):
        # Método que será sobrescrito pelas subclasses
        raise NotImplementedError("As subclasses devem implementar este método")


class Cachorro(Animal):
    def emitir_som(self):
        return "Au au!"


class Gato(Animal):
    def emitir_som(self):
        return "Miau!"


class Pato(Animal):
    def emitir_som(self):
        return "Quack!"


lista_de_animais = [Cachorro(), Gato(), Pato()]

# Iterando sobre a lista e chamando o mesmo método uniformemente
print("Os animais estão fazendo barulho:")
print("-" * 30)

for animal in lista_de_animais:
    nome_da_classe = type(animal).__name__
    som = animal.emitir_som()

    print(f"O {nome_da_classe} faz: {som}")