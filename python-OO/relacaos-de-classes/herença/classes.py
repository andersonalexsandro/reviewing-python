class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        print(f"{self.__class__.__name__} está falando")

class Aluno(Pessoa):
    ...


class Cliente(Pessoa):
    ...