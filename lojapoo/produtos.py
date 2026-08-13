from banco import conectar

def inserir_produto_inicial():
    """Insere os dados iniciais na tabela produtosL caso esteja vazia."""
    conexao = conectar()
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
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        cursor.execute("SELECT * FROM produtosL")
        produtos = cursor.fetchall()
        cursor.close()
        conexao.close()
        return produtos

def atualizar_produto_3():
    """Atualização do ID 3: preço = 89.90."""
    conexao = conectar()
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
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor()
        sql = "UPDATE produtosL SET preco = %s, quantidade = %s WHERE id = %s"
        cursor.execute(sql, (79.90, 25, 4))
        conexao.commit()
        cursor.close()
        conexao.close()
        print("Produto ID 4 atualizado!")