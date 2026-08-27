# Cria a aplicação flask
from flask import Flask, render_template

app = Flask(__name__)

# Define uma rota
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/produtos")
def produtos():
    return render_template(template_name_or_list= "produtos.html")

@app.route("/sobre")
def sobre():
    return "Esta é a página sobre."


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
