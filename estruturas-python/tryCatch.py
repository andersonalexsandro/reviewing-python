num1 = input("Digite um número ")
num2 = input("Digite outro número ")

try:
    num1 = int(num1)
    num2 = int(num2)
    print("Soma é igual a: ", num1 + num2)
except ValueError as erro:
    print("Erro ao converter os valores para inteiro:", erro)


# def divide(n1, n2):
#     try:
#         n1 / n2
#     except ZeroDivisionError as error:
#         print(error)
#         raise




