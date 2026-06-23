print("== SISTEMA DE LOGIN ==")

usuario_correto = "laura_mafra"
senha_correta = "1234"

tentativa = 5

while tentativa > 0:
    user = input("Digite seu usuário: ")
    senha = input("Digite sua senha: ")

    if user == usuario_correto and senha == senha_correta:
        print("\nLogin efetuado com sucesso! Bem-vindo.")
        break
    else:
        tentativa -= 1

        if tentativa > 0:
            print(f"Usuário ou Senha incorretos, restam {tentativa} tentativas!\n")

if tentativa == 0:
    print("\nAcesso bloqueado. Você excedeu o limite de 5 tentativas.")