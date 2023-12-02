from classes import Pessoa, Aluno, Cliente

c1 = Cliente("Anderson", 19)
a1 = Aluno("Beatriz", 19)
p1 = Pessoa("Anderson", 19)

print(c1.nome)
print(a1.nome)
c1.falar()
a1.falar()
p1.falar()