import vendas.calc_preco

valor = 100
porcentagem = 10

preco_com_aumento = vendas.calc_preco.aumenta_preco(preco=valor, porcentagem=porcentagem)
preco_com_desconto = vendas.calc_preco.diminui_preco(preco=valor, porcentagem=porcentagem)
print(f'preço com aumento:{preco_com_aumento}')
print(f'preço com desconto:{preco_com_desconto}')