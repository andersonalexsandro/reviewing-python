def aumenta_preco(preco, porcentagem):
    preco = preco + (preco * (porcentagem/100))
    return preco

def diminui_preco(preco, porcentagem):
    preco = preco - (preco * (porcentagem/100))
    return preco
