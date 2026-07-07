class Paciente:
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.__cpf = cpf
        self.__idade = idade
        self.__historico = []

    def get_cpf(self):
        cpf = self.__cpf
        return f"***.***.{cpf[7:10]}-{cpf[10:]}"

    def get_idade(self):
        return self.__idade

    def get_historico(self):
        return self.__historico

    # Setter
    def set_idade(self, nova_idade):
        if nova_idade > 0:
            self.__idade = nova_idade
        else:
            print("Idade inválida")

    def adicionar_historico(self, diagnostico):
        self.__historico.append(diagnostico)
        print(f"Diagnóstico registrado: {diagnostico}")

    def exibir_prontuario(self):
        print("=" * 30)
        print(f"Paciente: {self.nome}")
        print(f"Cpf: {self.get_cpf()}")
        print(f"Idade: {self.get_idade()}")
        print("Historico:")

        if len(self.__historico):
            for item in self.__historico:
                print(f"- {item}")
        else:
            print("Nenhum diagnóstico foi encontrado")

        print("=" * 30)


# Cadastrando novo paciente e adicionando no histórico
p1 = Paciente("Joao", "12345678910", 30)
p1.adicionar_historico("Gripe")
p1.adicionar_historico("Febre")

# Atualizando idade
p1.set_idade(31)

# Exibindo prontuário atualizado
p1.exibir_prontuario()
