from MatrizCiudades import MatrizCiudades
from ListaUnidades import ListaUnidades
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from ListaRobots import *
from PIL import Image, ImageTk



class Ciudad():
    def __init__(self, nombre, filas, columnas):
        self.nombre = nombre
        self.filas = filas
        self.columnas = columnas
        self.MatrizCiudades = MatrizCiudades()
        self.ListaUnidades = ListaUnidades()
        self.siguiente = None
        self.anterior = None
        self.ContadorUnidadCivil = 0

    def agregarMatrizCiudades(self, MatrizCiudades):
        self.MatrizCiudades.insertar(MatrizCiudades)
    
    def agregarListaUnidades(self, ListaUnidades):
        self.ListaUnidades.insertar(ListaUnidades)
    
    def getNombre(self):
        return self.nombre
    
    

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
            actual = actual.siguiente
    
    def MisionRescate(self):
        global listarobotsCiudades
        global ContadorUnidad
        ContadorChapinRescue=0
        global VentanaNuevaMision
        print("Mision de Rescate")
        ContadorChapinRescue = listarobotsCiudades.ContadorChapinFighter
        
      
        if ContadorChapinRescue == 0:
            messagebox.showinfo("Error", "No hay robot ChapinRescue")
        elif ContadorUnidad == 0:  
            messagebox.showinfo("Error", "No hay unidad Civil")
        else:
            VentanaNuevaMision.destroy()
            VentanaRescue = Tk()
            VentanaRescue.title("Mision de Rescate")
            VentanaRescue.geometry("300x300")
            VentanaRescue.config(bg = "SkyBlue1")
            Label(VentanaRescue, text = "Menú Mision de Rescate", font=("Arial", 16, "italic"),  bg="SkyBlue1").grid(pady=50, row=0, column=0)
            VentanaRescue.mainloop()
        

    def MisionExtraccion():
        print("Mision de Extracción de Recursos")

    def NuevaMision(self):
        global  listasCiudades
        global VentanaElegirCiudad
        global VentanaNuevaMision
        global ContadorUnidad
        ContadorUnidad = 0
        CiudadSeleccionada = listasCiudades.get()
        VentanaElegirCiudad.destroy()
        actual = self.cabeza
        while actual:
            if CiudadSeleccionada == actual.nombre:
                print(actual.ContadorUnidadCivil)
                actual.MatrizCiudades.graficarNeato(CiudadSeleccionada)
                ContadorUnidad = actual.ContadorUnidadCivil
            actual = actual.siguiente

        VentanaNuevaMision = Toplevel()
        VentanaNuevaMision.title("Nueva Mision")
        VentanaNuevaMision.geometry("900x900")
        VentanaNuevaMision.config(bg = "SkyBlue1")
        #ImagenCiudad = PhotoImage(file="matriz_"+CiudadSeleccionada+".png")
        #ImagenCiudad = ImagenCiudad.subsample(2,2)
        ImagenCiudad = Image.open("matriz_"+CiudadSeleccionada+".png") #abrir imagen
        ResizeImagen = ImagenCiudad.resize((700,700), Image.ANTIALIAS)
        ImagenCiudad = ImageTk.PhotoImage(ResizeImagen)
        LabelImagen = Label(VentanaNuevaMision, image = ImagenCiudad,bg="SkyBlue1",borderwidth=0)
        LabelImagen.place(x=25,y=100,width=700,height=700) 

        Label(VentanaNuevaMision, text = "Menú Misiones", font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=200,y=25,width=600)
        Button(VentanaNuevaMision, text="Misión de Rescate", width=30, height=1, font=("Arial", 12, "italic"), command=self.MisionRescate).place(x=100,y=850,width=300)
        Button(VentanaNuevaMision, text="Misión de Extracción de Recursos", width=30, height=1, font=("Arial", 12, "italic"), command=self.MisionExtraccion).place(x=500,y=850,width=300)
        VentanaNuevaMision.mainloop()
    
    def elegirciudad (self, listarobots):
        global listarobotsCiudades
        global listasCiudades
        global VentanaElegirCiudad
        actual = self.cabeza
        ultimo = self.cola

        listarobotsCiudades = listarobots
        

        VentanaElegirCiudad = Tk()
        VentanaElegirCiudad.title("Elegir Ciudad")
        VentanaElegirCiudad.geometry("300x300")
        VentanaElegirCiudad.config(bg = "SkyBlue1")
        Label(VentanaElegirCiudad, text = "Menú Ciudades", font=("Arial", 16, "italic"),  bg="SkyBlue1").grid(pady=50, row=0, column=0)
        Button(VentanaElegirCiudad, text="Planear Misión", width=30, height=1, font=("Arial", 12, "italic"), command=self.NuevaMision).grid(pady=5,padx=5, row=2, column=0)
        listasCiudades = ttk.Combobox(VentanaElegirCiudad, font=("Arial", 12, "italic"), width=20, height=5,state="readonly")
        ciudad = ''
        while actual: #"Ciudad1","Ciudad2","Ciudad3"
            if ultimo.nombre == actual.nombre:
                ciudad +=actual.nombre
            else:
                ciudad += actual.nombre+','
            actual = actual.siguiente
        ciudad = ciudad.split(",")
        listasCiudades.config(values=ciudad) 
        
                                          
        listasCiudades.current(0)
        listasCiudades.grid(pady=5,padx=5, row=1, column=0)
        VentanaElegirCiudad.mainloop()

    


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