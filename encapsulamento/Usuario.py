class Usuario:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.__senha = None

    # Setter
    def set_senha(self, nova_senha):
        if len(nova_senha) >= 6:
            self.__senha = nova_senha
            print("Senha alterada com sucesso!")
        else:
            print("Erro: A senha deve ter pelo menos 6 caracteres. A senha não foi alterada.")

    # Métodos
    def verificar_senha(self, senha_digitada):
        if senha_digitada == self.__senha:
            return True
        else:
            return False

    def exibir_perfil(self):
        print(f"Nome: {self.nome}")
        print(f"Email: {self.email}")
        print("Senha: ******")
        print("=" * 30)


# --- INSTANCIANDO E TESTANDO CONFORME O ENUNCIADO ---

# 1. Instanciar um usuário
u1 = Usuario("Laura", "imlauramafra@gmail.com")

# 2. Tentar definir senha inválida
u1.set_senha("1234")  # Vai avisar que é curta
print("-" * 30)

# 3. Tentar definir senha válida
u1.set_senha("123456")  # Vai aceitar
print("-" * 30)

# 4. Verificar o acesso com senha CORRETA e ERRADA
print("Testando senha correta (123456):", u1.verificar_senha("123456"))  # Retorna True
print("Testando senha errada (senha123):", u1.verificar_senha("senha123"))  # Retorna False
print("-" * 30)

# 5. Exibir o perfil ao final
u1.exibir_perfil()