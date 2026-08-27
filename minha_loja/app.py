# Cria a aplicação flask
from flask import Flask, render_template

app = Flask(__name__)

# Lista de produtos (simulando um banco de dados)
produtos_lista = [
    {"id": 1, "nome": "Kit descartáveis para festa (50 unidades)", "preco": 50.00, "categoria": "Festas"},
    {"id": 2, "nome": "Jogo de tabuleiro Ludo", "preco": 120.00, "categoria": "Brinquedos"},
    {"id": 3, "nome": "Toalha de mesa plastificada (metro)", "preco": 20.00, "categoria": "Casa"},
    {"id": 4, "nome": "Balão metalizado nº 9", "preco": 8.50, "categoria": "Festas"},
    {"id": 5, "nome": "Copo descartável 300ml (pacote c/ 25)", "preco": 12.00, "categoria": "Festas"},
    {"id": 6, "nome": "Vela de aniversário número", "preco": 6.00, "categoria": "Festas"},
]

# Define uma rota
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html", produtos=produtos_lista)

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")


# PASSANDO VALORES PELA URL
@app.route("/produto/<int:id>")
def produto(id):
    return f"Exibindo produto com id {id}"

@app.route("/categoria/<nome>")
def categoria(nome):
    return f"Categoria do produto: {nome}"


# Inicia o servidor

if __name__ == "__main__":
    app.run(debug=True)
