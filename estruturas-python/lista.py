string = "O Brasil é penta"
lista = string.split(" ")
string2 = " ".join(lista)

print(string)
print(lista)
print(string2)

print()

for indice, valor in enumerate(lista):
    print(f"Valor: {valor}, indice: {indice}")

lista2 = [
    [0, "Anderson"],
    [1, "Beatriz"],
    [2, "Carlos"]
]

for indice, nome in lista2:
    print(indice, nome)

lista3 = ["Anderson","Beatriz","Carlos"]


for indice, nome in enumerate(lista3):
    print(indice, nome)