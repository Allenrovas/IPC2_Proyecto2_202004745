from MatrizCiudades import MatrizCiudades
from ListaUnidades import ListaUnidades

class Ciudad():
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.MatrizCiudades = MatrizCiudades()
        self.ListaUnidades = ListaUnidades()
        self.siguiente = None
        self.anterior = None

    def agregarMatrizCiudades(self, MatrizCiudades):
        self.MatrizCiudades.insertar(MatrizCiudades)
    
    def agregarListaUnidades(self, ListaUnidades):
        self.ListaUnidades.insertar(ListaUnidades)
    
    

class ListaCiudades(object):
    def __init__(self):
        self.cabeza =  None
        self.cola = None
        self.contador = 0


    def insertar(self,  nodo):
        nodo = nodo

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
        
        while actual:
            print(actual.nombre)
            actual.patrones.recorrer()
            actual = actual.siguiente
    
    def recorrermenu(self):
        actual =self.cabeza
        i=1
        SeleccionarPiso = ""
        print("======Menu Pisos======")
        while actual:
            print(" ",actual.nombre)
            i+=1
            actual = actual.siguiente
        print(" exit. Regresar al menu principal")
        SeleccionarPiso = input("Ingrese el nombre del piso a graficar: ")
        actual = self.cabeza

        while actual:
            if SeleccionarPiso == actual.nombre:
                actual.patrones.cabeza.casillas.graficar()
                actual.patrones.recorrermenu()
            elif SeleccionarPiso == "exit":
               exit
            else:
                "Ingrese una entrada válida"
            actual = actual.siguiente