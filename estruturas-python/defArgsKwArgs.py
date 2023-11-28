def funcao(*args, **kwrgs):
    print(args)
    print(kwrgs.get("nome"))


lista = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
funcao(*lista, *lista2, nome="Anderson")