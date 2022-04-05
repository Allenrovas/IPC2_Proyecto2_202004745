class Robots():
    def __init__(self, nombre, tipo, capacidad):
        self.nombre = nombre
        self.tipo = tipo
        self.capacidad = capacidad
        self.siguiente = None
        self.anterior = None
        
class ListaRobots(object):
    def __init__(self):
        self.cabeza =  None
        self.cola = None
        self.contador = 0
        self.ContadorChapinRescue = 0
        self.ContadorChapinFighter = 0

    def recorrer(self):
        actual = self.cabeza
        
        while actual is not None:
            print(actual.nombre)
            actual = actual.siguiente
        print(self.contador)

    def insertar(self, nombre, tipo, capacidad):
        nodo = Robots(nombre, tipo, capacidad)

        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        
        self.contador += 1
        if nodo.tipo == "ChapinRescue":
            self.ContadorChapinRescue += 1
        elif nodo.tipo == "ChapinFighter":
            self.ContadorChapinFighter += 1

        
    

        