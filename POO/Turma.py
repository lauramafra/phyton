class Turma:

    # Atributos
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    # Métodos

    # matricular
    def matricular(self, nome_do_aluno):
        if nome_do_aluno in self.alunos:
            print(f"Aviso: O aluno {nome_do_aluno} já está matriculado nesta turma!")
        else:
            self.alunos.append(nome_do_aluno)
            print(f"Aluno {nome_do_aluno} matriculado com sucesso.")

    # remover
    def remover(self, nome_do_aluno):
        if nome_do_aluno in self.alunos:
            self.alunos.remove(nome_do_aluno)
            print(f"Aluno {nome_do_aluno} removido da turma.")
        else:
            print(f"Erro: O aluno {nome_do_aluno} não foi encontrado para remoção.")

    # listar
    def listar_alunos(self):
        lista_ordenada = sorted(self.alunos)
        total_alunos = len(self.alunos)

        print(f"\n--- Lista de Alunos da Turma {self.nome} ---")
        for aluno in lista_ordenada:
            print(f"- {aluno}")
        print(f"Total de alunos matriculados: {total_alunos}\n")

        return self.alunos


    def esta_matriculado(self, nome_do_aluno):
            if nome_do_aluno in self.alunos:
                print(f"O aluno {nome_do_aluno} está matriculado na turma {self.nome}.")
                return True
            else:
                print(f"O aluno {nome_do_aluno} NÃO está matriculado na turma {self.nome}.")
                return False


# Criando a turma e matriculando 5 alunos
t1 = Turma("2931")
t1.matricular("Laura")
t1.matricular("Luca")
t1.matricular("Luis")
t1.matricular("Leonardo")
t1.matricular("Lara")

# Tentando matricular um nome repetido
t1.matricular("Laura")

# Mostrando a lista
t1.listar_alunos()  # Agora esse método já faz o print internamente!

# Removendo
t1.remover("Lara")

# Exibindo a lista final
t1.listar_alunos()

# Verificando se o aluno removido ainda consta na turma
t1.esta_matriculado("Lara")