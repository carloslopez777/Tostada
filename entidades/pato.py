class Pato:
    def __init__ (self, peso, altura, velocidad):
        self.peso = peso
        self.altura = altura
        self.velocidad = velocidad
        
    def saludar(self):
        return f"Hola, peso {self.peso} kg, mido {self.altura} cm y corro demasiado {self.velocidad}."