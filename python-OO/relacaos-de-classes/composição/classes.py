class Cliente:

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.enderecos = []

    def inserir_endereco(self, estado, cidade):
        self.enderecos.append(Endereco(estado, cidade))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.estado, endereco.cidade)

    def __del__(self):
        print(f'{self.nome} foi apagado')


class Endereco:
    def __init__(self, estado, cidade):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.estado}/{self.cidade} foi apagado')
