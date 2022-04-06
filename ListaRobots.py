
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

    def recorrerRescate(self):
        actual = self.cabeza
        ultimo = self.cola
        Nombre = ""
        while actual is not None:
            if actual.tipo == "ChapinRescue":
                if ultimo == actual:
                    Nombre += actual.nombre
                else:
                    Nombre += actual.nombre +","
            else: 
                pass
            actual = actual.siguiente
        return Nombre
    
    def recorrerRecursos(self):
        actual = self.cabeza
        ultimo = self.cola
        Nombre = ""
        while actual is not None:
            if actual.tipo == "ChapinFighter":
                if ultimo == actual:
                    Nombre += actual.nombre
                else:
                    Nombre += actual.nombre +","
            else: 
                pass
            actual = actual.siguiente
        return Nombre
    
    

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

        
    

        