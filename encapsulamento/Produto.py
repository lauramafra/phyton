class Produto:
    def __init__(self, nome, preco, estoque_inicial=0):
        self.nome = nome
        self.preco = preco
        self.__estoque = estoque_inicial

    #Getter
    def get_estoque(self):
        return self.__estoque

    #Métodos
    def adicionar_estoque(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
            print(f"{quantidade} unidades de '{self.nome}' adicionadas ao estoque.")
        else:
            print("Erro: A quantidade para adicionar deve ser maior que zero.")

    def vender(self, quantidade):
        if quantidade <= 0:
            print("Erro: A quantidade de venda deve ser maior que zero.")
        elif quantidade <= self.__estoque:
            self.__estoque -= quantidade
            print(f"Venda de {quantidade} unidades de '{self.nome}' realizada com sucesso!")
        else:
            print(f"Aviso: Estoque insuficiente de '{self.nome}' para vender {quantidade} unidades. (Estoque atual: {self.__estoque})")

    def exibir_info(self):
        print(f"Produto: {self.nome}")
        print(f"Preço: R$ {self.preco:.2f}")
        print(f"Estoque Atual: {self.get_estoque()} unidades")
        print("=" * 40)



# Criando dois produtos
p1 = Produto("Notebook", 3500.00, 10)
p2 = Produto("Mouse Gamer", 150.00, 5)

# Simulando operações no Produto 1
p1.vender(3)          # Venda bem-sucedida (sobra 7)
p1.adicionar_estoque(5) # Adiciona estoque (vai para 12)
p1.vender(15)         # Estoque insuficiente!
p1.exibir_info()

# Simulando operações no Produto 2
p2.vender(6)          # Estoque insuficiente!
p2.adicionar_estoque(-2) # Erro: quantidade inválida
p2.vender(4)          # Venda bem-sucedida (sobra 1)
p2.exibir_info()