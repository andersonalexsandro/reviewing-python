from classes import Escritor
from classes import Caneta
from classes import Maquina_de_Escrever

maquina = Maquina_de_Escrever("Roxa")
caneta = Caneta("Preta")
escritor = Escritor("Anderson", caneta)
escritor.ferramenta.escrever()
escritor.ferramenta = maquina
escritor.escrever()