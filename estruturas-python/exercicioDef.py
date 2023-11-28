def ola_mundo():
    return "Olá mundo"

def mestre(funcao):
    return funcao()

executando = mestre(ola_mundo)
print(executando)

print("############################")

def mestre(funcao, *args):
    return funcao(*args)

def fala_oi(nome):
    return f'Oi {nome}'

def saudacao(nome, saudacao):
    return f'{saudacao} {nome}'

executando = mestre(fala_oi, "Anderson")
print(executando)

executando = mestre(saudacao, "Anderson", "Bom dia")
print(executando)


