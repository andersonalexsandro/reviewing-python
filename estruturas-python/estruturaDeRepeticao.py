x = 0
while x < 10:
    print(x)
    x+=1

palavra = "palavra"
for letra in palavra:
    print(letra, end="-")

print()

for n, letra in enumerate(palavra):
    print(n, letra , sep="-")

for n in range(10):
    print(n)