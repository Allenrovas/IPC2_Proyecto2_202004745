class Nodo_Cabecera():
    def __init__(self, id):
        self.id = id
        self.siguiente = None
        self.anterior = None
        self.acceso = None

    def getAcceso(self):
        return self.acceso

    def setAcceso(self, nuevo_acceso):
        self.acceso = nuevo_acceso

class Lista_Cabecera():
    def __init__(self, tipo):
        self.primero = None
        self.ultimo = None
        self.tipo = tipo # si son Columnas o Filas
        self.size = 0

    
    def insertar_nodoCabecera(self, nuevo : Nodo_Cabecera):
        self.size += 1
        if self.primero == None:
            self.primero = nuevo
            self.ultimo = nuevo
        else:
            # ---- Insercion en ORDEN
            # -- verificamos si el nuevo es menor que el primero
            if nuevo.id < self.primero.id:
                nuevo.siguiente = self.primero
                self.primero.anterior = nuevo
                self.primero = nuevo
            # -- verificamos si el nuevo es mayor que el ultimo
            elif nuevo.id > self.ultimo.id:
                self.ultimo.siguiente = nuevo
                nuevo.anterior = self.ultimo
                self.ultimo = nuevo
            else:
                # -- sino, recorremos la lista para buscar donde acomodarnos, entre el primero y el ultimo
                tmp: Nodo_Cabecera = self.primero 
                while tmp != None:
                    if nuevo.id < tmp.id:
                        nuevo.siguiente = tmp
                        nuevo.anterior = tmp.anterior
                        tmp.anterior.siguiente = nuevo
                        tmp.anterior = nuevo
                        break
                    elif nuevo.id > tmp.id:
                        tmp = tmp.siguiente
                    else:
                        break

    
    def mostrarCabeceras(self):
        tmp = self.primero
        while tmp != None:
            print('Cabecera', self.tipo, tmp.id)
            tmp = tmp.siguiente
            

    def getCabecera(self, id) -> Nodo_Cabecera: #esta funcion debe retornar un nodo cabecera
        tmp = self.primero
        while tmp != None:
            if id == tmp.id:
                return tmp
            tmp = tmp.siguiente
        return None
