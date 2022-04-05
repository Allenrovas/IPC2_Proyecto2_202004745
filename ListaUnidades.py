class UnidadMilitar():
    def __init__(self, fila, columna, Combate):
        self.fila = fila
        self.columna = columna
        self.Combate = Combate
        self.siguiente = None
        self.anterior = None
  

class ListaUnidades(object):
    def __init__(self):
        self.cabeza =  None
        self.cola = None
        self.contador = 0


    def insertar(self,  fila, columna, Combate):
        nodo = UnidadMilitar(fila, columna, Combate)

        if self.cabeza is None:
            self.cabeza = nodo
            self.cola = self.cabeza
        else:
            nodo.anterior = self.cola
            self.cola.siguiente = nodo
            self.cola = nodo
        
        self.contador += 1
    
    def recorrer(self):
        actual = self.cabeza
        
        while actual is not None:
            print(actual.nombre)
            actual = actual.siguiente