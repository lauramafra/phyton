print ("== SISTEMA DE VOTAÇÃO ==")

joao =0

ana =0

pedro =0

print ("== SISTEMA DE VOTAÇÃO ==")
print("Candidatos:")
print("1- João")
print("2- Ana")
print("3- Pedro")

while True:
    voto = int(input("1-João, 2-Ana, 3-Pedro, 4-Encerrar: "))

    if voto == 4:
        break
    elif voto == 1:
        joao += 1
    elif voto == 2:
        ana += 1
    elif voto == 3:
        pedro += 1

# Calcula o total
total = joao + ana + pedro

#  quem ganhou
if joao > ana and joao > pedro:
    vencedor = "João"
elif ana > joao and ana > pedro:
    vencedor = "Ana"
else:
    vencedor = "Pedro"

# Exibe o resultado final
print("\nRESULTADO DA ELEIÇÃO")
print(f"Ana: {ana}")
print(f"João: {joao}")
print(f"Pedro: {pedro}")
print(f"Total de votos: {total}")
print(f"Vencedor(a): {vencedor}")