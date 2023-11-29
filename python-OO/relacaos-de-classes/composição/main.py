from classes import Cliente, Endereco

cliente1 = Cliente("Anderson", 19)
cliente1.inserir_endereco("PE", "Recife")
cliente1.inserir_endereco("PB", "Rio Tinto")
cliente1.listar_enderecos()
print("#" * 100)
