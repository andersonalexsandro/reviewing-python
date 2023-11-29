class Pessoa:

    #variável estática
    ano_atual = 2023

    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo=comendo
        self.falando=falando

    def falar(self):
        print( self.nome, "está falando...")

    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)