l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel * 2 for variavel in l1]
l3 = [(v1 + v2) for v1 in l1 for v2 in range(3)]
print(l2)
print(l3)

lista = [
    ("chave", "valor"),
    ("cahve2", "valor2")
]

d1 = {x: y for x, y in lista}
print(d1)