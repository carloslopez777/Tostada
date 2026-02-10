class Pinguino:
    def __init__ (self, nombre, edad, altura, velocidad):
        self.nombre = nombre
        self.edad = edad
        self.altura = altura
        self.velocidad = velocidad
        
    def calcular_destreza(self):
        if self.velocidad < 100:
            print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años, mido {self.altura} cm y corro {self.velocidad} m/s, soy muy lento.")
        elif self.velocidad > 100 or self.velocidad < 500:
            print(print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años, mido {self.altura} cm y corro {self.velocidad} m/s, voy caminando normal."))
        else:
            print(f"Hola, me llamo {self.nombre}, tengo {self.edad} años, mido {self.altura} cm y corro {self.velocidad} m/s, soy demasiado rápido.")    
        