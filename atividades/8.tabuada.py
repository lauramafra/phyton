print("== TABUADA ==")

numero= int(input("Digite um número:"))

print(f"\nTabuada do {numero}:")

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
