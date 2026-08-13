from banco import conectar

def relatorio_por_categoria(categoria='Vestuário'):
    """1. Seleciona produtos da categoria informada."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        sql = "SELECT * FROM produtosL WHERE categoria = %s"
        cursor.execute(sql, (categoria,))
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultados

def relatorio_preco_maior_que(valor=50):
    """2. Seleciona nome e preco onde preco > valor."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        sql = "SELECT nome, preco FROM produtosL WHERE preco > %s"
        cursor.execute(sql, (valor,))
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultados

def relatorio_preco_entre(min_val=20, max_val=100):
    """3. Seleciona produtos com preco entre min_val e max_val."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        sql = "SELECT * FROM produtosL WHERE preco BETWEEN %s AND %s"
        cursor.execute(sql, (min_val, max_val))
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultados

def relatorio_busca_por_nome(termo='A'):
    """4. Seleciona produtos cujo nome contém determinado termo (LIKE)."""
    conexao = conectar()
    if conexao:
        cursor = conexao.cursor(dictionary=True)
        sql = "SELECT * FROM produtosL WHERE nome LIKE %s"
        cursor.execute(sql, (f'%{termo}%',))
        resultados = cursor.fetchall()
        cursor.close()
        conexao.close()
        return resultados