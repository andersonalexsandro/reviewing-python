multiplica = lambda x, y: x * y
print(multiplica(2,3))

print()
print("######################################################")
print()

lista = [
    ['P1', 13],
    ["P2", 6],
    ['P3', 7],
    ['P4', 50],
    ['P5', 8],
]

def func(item):
    return item[1]

lista.sort(key=func)
print(lista)

print()
print("######################################################")
print()

lista.sort(key=lambda item: item[1])
print(lista)
print(sorted(lista, key=lambda item: item[1]))

print()
print("######################################################")
print()

produtos = [
    {"nome": "p1", "preco": 13},
    {"nome": "p2", "preco": 55.55},
    {"nome": "p3", "preco": 5.99},
    {"nome": "p4", "preco": 16.12},
    {"nome": "p5", "preco": 12},
    {"nome": "p6", "preco": 17},
]

pessoas = [
    {"nome": "And", "idade": 19},
    {"nome": "bia", "idade": 20},
    {"nome": "ana", "idade": 16},
    {"nome": "nano", "idade": 20},
    {"nome": "uno", "idade": 22},
    {"nome": "ino", "idade": 20},
]

lista_numerica = [1,2,3,4,5,6,7,8,9]


nova_lista = map(lambda x: (x*2), lista_numerica)
nova_lista = [x * 2 for x in lista_numerica]
nova_lista_pessoas = map( lambda x: x["nome"], pessoas)
print(list(nova_lista_pessoas))
