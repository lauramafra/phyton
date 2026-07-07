class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.__nota = None
        self.set_nota(nota)

    # Getter
    def get_nota(self):
        return self.__nota

    # Setter
    def set_nota(self, nota):
        if 0 <= nota <= 10:
            self.__nota = nota
        else:
            print("Nota inválida. Digite um valor entre 0 e 10")

    def situacao(self):
        if self.__nota is None:
            return "Sem nota cadastrada"
        elif self.__nota >= 6:
            return "Aprovado"
        else:
            return "Reprovado"

    def exibir_info(self):
        print(f"Aluno: {self.nome}")
        print(f"Nota: {self.get_nota()}")
        print(f"Situação: {self.situacao()}")
        print("="*30)

# Cadastrando alunos
a1 = Aluno("Laura", 10)
a1.exibir_info()

a2 = Aluno("Luis", 8)
a2.exibir_info()

a2.set_nota(5)
a2.exibir_info()