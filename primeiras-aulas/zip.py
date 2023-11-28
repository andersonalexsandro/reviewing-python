cidades =["Sao paulo", "Belo Horizonte", "Salvador", "Monte Belo"]

estados = ["SP", "MG", "BA"]

cidade_estado = zip(estados, cidades)
print(dict(cidade_estado))


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
l2 = [variavel * 2 for variavel in l1]

lista_soma = [x + y for x, y in zip(l1, l2)]
print(lista_soma)