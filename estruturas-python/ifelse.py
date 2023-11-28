jovem = 25
adulto = 55
velho = 120
idade = int(input("Digite sua idade: "))

if (idade <= jovem):
    print("Jovem")
elif (idade <= adulto):
    print("Adulto")
elif (idade <= velho):
    print("Velho")