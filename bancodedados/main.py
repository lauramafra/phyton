from config import DB_CONFIG
import mysql.connector

conexao = None
try:
    conexao = mysql.connector.connect(**DB_CONFIG)
    cursor = conexao.cursor()

    cursor.execute(""
        create table if not exists produtos(
        id int auto.increment primary key,

    )
    "")

    conexao.commit()
    print("Tabela criada com sucesso")

    except mysql.connector.Error as erro:
        print(f"Erro: {erro}")

    finally if conexao and conexao.is_connected():
        conexao.close()