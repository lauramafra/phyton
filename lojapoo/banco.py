import mysql.connector
from config import DB_CONFIG


def conectar():
    """Estabelece a conexão com o banco de dados loja."""
    try:
        conexao = mysql.connector.connect(**DB_CONFIG)
        return conexao
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao banco de dados: {err}")
        return None


def criar_tabela():
    """Cria a tabela produtosL e ajusta as colunas conforme a especificação."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()

        # Criação da tabela produtosL
        sql_tabela = """
        CREATE TABLE IF NOT EXISTS produtosL (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nome VARCHAR(100) NOT NULL,
            preco DECIMAL(10,2),
            quantidade INT,
            categoria VARCHAR(50)
        );
        """
        cursor.execute(sql_tabela)
        conexao.commit()

        cursor.close()
        conexao.close()