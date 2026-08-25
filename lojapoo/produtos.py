from bancodedados.config import DB_CONFIG
from models import Produto
import mysql.connector

def inserir_produto_inicial():

    conexao = None
    if conexao:
        cursor = conexao.cursor()
        cursor.execute("SELECT COUNT(*) FROM produtosL")
        if cursor.fetchone()[0] == 0:
            sql = """
            INSERT INTO produtosL (nome, preco, quantidade, categoria) 
            VALUES (%s, %s, %s, %s)
            """
            valores = [
                ('Camiseta Algodão Básica', 49.90, 50, 'Vestuário'),
                ('Calça Jeans Slim', 139.90, 30, 'Vestuário'),
                ('Smartphone Android 128GB', 1499.00, 15, 'Eletrônicos'),
                ('Fone de Ouvido Sem Fio', 199.90, 40, 'Eletrônicos'),
                ('Arroz Integral 1kg', 7.50, 100, 'Alimentos')
            ]
            cursor.executemany(sql, valores)
            conexao.commit()
            print("Produtos iniciais inseridos com sucesso!")
        cursor.close()
        conexao.close()

def listar_todos_produtos():
    """Retorna todos os produtos (SELECT * FROM produtosL)."""
    conexao = None
    if conexao:
        cursor = mysql.connector.connect(**DB_CONFIG)
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM produtosL ORDER BY nome")
        return[Produto.reverte_tupla(linha) for linha in cursor.fetchall()]
    except mysql.connector.Error as erro:
        print(f"Erro ao Listar: {erro}")
    finally:
        if conexao and conexao.is_connected():
        conexao.close()

def atualizar_produto_3():
    """Atualização do ID 3: preço = 89.90."""
    conexao = None
    if conexao:
        cursor = conexao.cursor()
        sql = "UPDATE produtosL SET preco = %s WHERE id = %s"
        cursor.execute(sql, (89.90, 3))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Produto ID 3 atualizado!")

def atualizar_produto_4():
    """Atualização do ID 4: preço = 79.90 e quantidade = 25."""
    conexao = None
    if conexao:
        cursor = conexao.cursor()
        sql = "UPDATE produtosL SET preco = %s, quantidade = %s WHERE id = %s"
        cursor.execute(sql, (79.90, 25, 4))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Produto ID 4 atualizado!")