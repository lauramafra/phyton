#Exemplo1
#Entrada de dados

idade = 18

altura = 1.75

nome ="João"

aprovado = True

frutas = {"maçã", "banana", "uva"}

cores = {"azul", "verde", "vermelho"}

aluno= {
    "nome": "Maria",
    "idade": 18,
    "curso": "Desenvolvimento de Sistemas",
}

#Saída de dados

print("Exemplo de tipo de dados em Phyton\n")

print("Idade:", idade)
print("Tipo:", type (idade))

print("\nAltura:", altura)
print("Tipo:", type(altura))

print("\nNome:", nome)
print("Tipo:", type(nome))

print("\nAprovado:", aprovado)
print("Tipo:", type(aprovado))

print("\nFrutas:", frutas)
print("Tipo:", type(frutas))

print("\nCores:", cores)
print("Tipo:", type(cores))

print("\nAluno:", aluno)
print("Tipo:", type(aluno))

#Exemplo 2
nome = input("Digite seu nome: ")

idade = int(input("Digite sua idade: "))

dinheiro = float(input("Digite sua quantia em dinheiro: "))

print(f"Nome: {nome} - \n{idade} anos - R$ {dinheiro}")

print("Nome:", nome,"\nIdade:", idade,"anos - R$", dinheiro)

