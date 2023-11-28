clientes = { "id1":"fulano", "id2": "beltrano", "id3": "ciclano", "id4": "deltrano"}

for k, v in clientes.items():
    print(f"Cliente de identificador: {k} se chama {v}")

for x in range (1, len(clientes) + 1, 1):
    key = "id" + str(x)
    print(clientes.get(key))