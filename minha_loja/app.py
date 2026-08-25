# Cria a aplicação flask
from flask import Flask

app = Flask(__name__)

# Define uma rota
@app.route("/")
def index():
    return "Bem-vindo(a) ao Lojão da aura."

app.route("/produtos")
def produtos():
    return ("Kit descartáveis para festa(50 UNIDADES) - R$ 50,00"
            "Jogo de tabuleiro Ludo - R$120,00"
            "Toalha de mesa plastificada - R$ 20,00 o metro")


# PASSANDO VALORES PELA URL
@app.route("/produto/<int:id>")
def produto(id):
    return f"Exibindo produto com id {id}"

@app.route("/sobre")
def sobre():
    return f"Esta página é sobre o Lojão da aura"



# Inicia o servidor

if __name__ == "__main__":
    app.run(debug=True)
