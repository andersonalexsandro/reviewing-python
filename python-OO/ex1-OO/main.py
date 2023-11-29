from pessoa import Pessoa

pessoa1 = Pessoa("Anderson", 19)
print(pessoa1.nome)
pessoa1.falar()
pessoa2 = Pessoa.por_ano_nascimento("Beatriz", 2003)
print(pessoa2.idade)