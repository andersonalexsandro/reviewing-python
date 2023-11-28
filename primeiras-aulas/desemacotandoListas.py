lista = ['Anderson', "Beatriz", "Carlos"]

n1, n2, n3 = lista

print(n1)
print(n2)
print(n3)

n1, n2, *lista_dos_restantes = lista

print(n1)
print(n2)
print(lista_dos_restantes)