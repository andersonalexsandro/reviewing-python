num1 = input("Digite um número ")
num2 = input("Digite outro número ")

try:
    num1 = int(num1)
    num2 = int(num2)
    print("Soma é igual a: ", num1 + num2)
except:
    print("Erro ao converter os valores para inteiro")
