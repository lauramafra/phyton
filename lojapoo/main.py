from banco import criar_tabela
from produtos import (
    inserir_produto_inicial,
    listar_todos_produtos,
    atualizar_produto_3,
    atualizar_produto_4
)
import relatorio


def exibir_resultados(titulo, lista_produtos):
    print(f"\n--- {titulo} ---")
    if not lista_produtos:
        print("Nenhum registro encontrado.")
        return
    for item in lista_produtos:
        print(item)


def main():
    # 1. Inicializa a tabela e dados
    criar_tabela()
    inserir_produto_inicial()

    # 2. Execução dos Relatórios (Consultas SQL)
    exibir_resultados("Todos os Produtos", listar_todos_produtos())

    # Consulta 1: Categoria Vestuário
    exibir_resultados("Produtos de Vestuário", relatorio.relatorio_por_categoria('Vestuário'))

    # Consulta 2: Preço > R$ 50,00
    exibir_resultados("Produtos com Preço > R$ 50,00", relatorio.relatorio_preco_maior_que(50))

    # Consulta 3: Preço entre R$ 20,00 e R$ 100,00
    exibir_resultados("Produtos com Preço Entre R$ 20,00 e R$ 100,00", relatorio.relatorio_preco_entre(20, 100))

    # Consulta 4: Nome com a letra 'A'
    exibir_resultados("Produtos com 'A' no nome", relatorio.relatorio_busca_por_nome('A'))

    # 3. Execução das Atualizações (UPDATEs)
    print("\n--- Executando Atualizações ---")
    atualizar_produto_3()
    atualizar_produto_4()

    # Exibição final atualizada
    exibir_resultados("Todos os Produtos (Após Atualizações)", listar_todos_produtos())


if __name__ == "__main__":
    main()