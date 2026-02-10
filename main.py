from entidades.gato import Gato
from entidades.pato import Pato
from entidades.pinguino import Pinguino

object1 = Gato("Anastacio", 3, "Negro con gris")
print (object1.saludar())

object2 = Pato(4, 40, "Rápido")
print (object2.saludar())

objetc3 = Pinguino("Felipe de Jesús", 48, 45, 230)
print (objetc3.calcular_destreza())