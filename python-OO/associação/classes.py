class Escritor:
    def __init__(self, nome, ferramenta):
        self.__nome = nome
        self.__ferramenta = ferramenta

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def ferramenta(self):
        return self.__ferramenta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self.__ferramenta = ferramenta

    def escrever(self):
        self.ferramenta.escrever()

    
class Caneta:

    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    def escrever(self):
        print(f"A caneta {self.cor} está escrevendo")

class Maquina_de_Escrever:

    def __init__(self, cor):
        self.__cor = cor

    @property
    def cor(self):
        return self.__cor
    
    @cor.setter
    def cor(self, cor):
        self.__cor = cor

    def escrever(self):
        print(f"A maquina {self.cor} está escrevendo")