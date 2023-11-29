class CarrinhoDeCompras:
    
    def __init__(self):
        self.prdutos = []

    def inserir_produto(self, produto):
        self.prdutos.append(produto)

    def listar_produtos(self):
        for produto in self.prdutos:
            print(produto.nome, produto.valor)

    def soma_total(self):
        soma = 0
        for produto in self.prdutos:
            soma += produto.valor
        return soma

class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor