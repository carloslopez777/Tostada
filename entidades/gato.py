class Gato:
    def __init__ (self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color
        
    def saludar(self):
        return f"Hola, me llamo {self.nombre}, tengo {self.edad} años y soy de color {self.color}."