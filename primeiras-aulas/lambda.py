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

