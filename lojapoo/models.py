class Produto:
    def __init__(self, nome, preco,quantidade, categoria ):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
        self.categoria = categoria

    def converte_tupla(self):
        return (self.nome, self.preco, self.quantidade, self.categoria)

    @staticmethod
    def reverte_tupla(tupla):
        