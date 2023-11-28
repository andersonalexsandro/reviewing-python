nome = "anderson"
idade = 19
altura = 1.70
peso = 75
is_maior = idade > 18

print("Nome:", nome)
print("idade:" , idade)
print("é maior de idade =" , is_maior)
print("peso:",peso)
imc = peso / (altura **2)

print("ICM: ", imc)

#################

x = 10
y = 100

x, y = y, x

z = 1000

x, y , z = z, x, y