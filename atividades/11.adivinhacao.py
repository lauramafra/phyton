import random

print("DUVIDO VOCÊ ADIVINHAR O NÚMERO QUE EU ESCOLHI!")

numero = random.randint(1,100)


while True:
    palpite = int(input("Dê um palpite (entre 1 e 100): "))

    if palpite == numero:
        print(f"Parabéns! Você acertou, o número era {numero}!")
        break  # O break encerra o jogo porque o usuário ganhou!

        # 3. Se não acertou, damos as dicas
    elif palpite < numero:
        print(f"O número correto é MAIOR que {palpite}")
    else:
        print(f"O número correto é MENOR que {palpite}")

