nome = "anderson"
idade = 19
altura = 1.70
peso = 75
is_maior = idade > 18
imc = peso / (altura **2)

print(f"{nome} tem {idade} anos, {altura}m de altura, pesa {peso}kg, {imc:.2f} de IMC")
print("{0} tem {1} anos, {2}m de altura, pesa {3}kg, {4} de IMC" .format(nome, idade, altura, peso, imc))
print("{n} tem {i} anos, {a}m de altura, pesa {p}kg, {imc} de IMC" .format(n=nome, i=idade, a=altura, p=peso, imc=imc))

num_1 = 1
print(f'{num_1:0>3}')
print(f'{num_1:0<3}')
print(f'{num_1:0^3}')


