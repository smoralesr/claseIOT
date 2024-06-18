class Persona():

    def __init__(self, nombre, edad):  
        self.nombre = nombre
        self.edad = edad
        self.texto = ''

    def saludar(self):
        self.texto = f"Hola {self.nombre}" 
    
    def presentarse(self):
        self.texto = f"Me llamo {self.nombre} y tengo {self.edad} años"

    def despedirse(self):
        self.texto = f"Adios {self.nombre}"