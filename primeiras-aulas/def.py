def isNomeValido(nome):
    if nome == None or (len(nome) < 3):
        return False
    
    for letra in nome:
        if(letra.isdigit()):
            return False
        
    return True

nome = input("Digite seu nome: ")

msg = "Nome válido" if isNomeValido(nome) else "Nome inválido"
print(msg)

