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
        self.ContadorUnidadMilitar = 0

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

    
    
    def MisionCompletada(self):
        global listasRobots
        global ListasCiviles
        global Entradas
        global VentanaNuevaMision
        global CiudadSeleccionada
        print("Finalizada")
        
        RobotSeleccionado = listasRobots.get()
        UnidadSeleccionada = ListasCiviles.get()
        Entrada = Entradas.get()
        VentanaNuevaMision.destroy()
        VentanaMision = Toplevel()
        VentanaMision.title("Nueva Mision")
        VentanaMision.geometry("1100x900")
        VentanaMision.config(bg = "SkyBlue1")
        
        #ImagenCiudad = PhotoImage(file="matriz_"+CiudadSeleccionada+".png")
        #ImagenCiudad = ImagenCiudad.subsample(2,2)
        ImagenCiudad = Image.open("matriz_"+CiudadSeleccionada+".png") #abrir imagen
        ResizeImagen = ImagenCiudad.resize((700,700), Image.ANTIALIAS)
        ImagenCiudad = ImageTk.PhotoImage(ResizeImagen)
        LabelImagen = Label(VentanaMision, image = ImagenCiudad,bg="SkyBlue1",borderwidth=0)
        LabelImagen.place(x=25,y=100,width=700,height=700) 
        

        Label(VentanaMision, text = "Misión Completada", font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=200,y=25,width=600)

        Label(VentanaMision, text = "Se eligió el robot:", font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=750,y=150,width=200) 
        Label(VentanaMision, text = RobotSeleccionado, font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=750,y=225,width=200) 

        Label(VentanaMision, text = "Se eligió la unidad:", font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=750,y=300,width=200)
        Label(VentanaMision, text = UnidadSeleccionada, font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=750,y=375,width=200)

        Label(VentanaMision, text = "Se eligió la entrada:", font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=750,y=450,width=200)
        Label(VentanaMision, text = Entrada, font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=750,y=525,width=200)
        VentanaMision.mainloop()
  

    def MisionRescate(self):
        global listarobotsCiudades
        global VentanaNuevaMision
        global  listasCiudades
        global VentanaElegirCiudad
        global VentanaNuevaMision
        global CiudadSeleccionada

        global listasRobots
        global ListasCiviles
        global Entradas

        Nombre = listarobotsCiudades.recorrerRescate()
        ContadorUnidad = 0
        actual = self.cabeza
        while actual:
            ContadorUnidad = actual.ContadorUnidadCivil
            actual = actual.siguiente
        ContadorChapinRescue=0
        
        print("Mision de Rescate")
        ContadorChapinRescue = listarobotsCiudades.ContadorChapinRescue
        
      
        if ContadorChapinRescue == 0:
            messagebox.showinfo("Error", "No hay robot ChapinRescue")
        elif ContadorUnidad == 0:  
            messagebox.showinfo("Error", "No hay unidad Civil")
        else:
            CiudadSeleccionada = listasCiudades.get()
            VentanaElegirCiudad.destroy()
            actual = self.cabeza
            while actual:
                if CiudadSeleccionada == actual.nombre:
                    print(actual.ContadorUnidadCivil)
                    actual.MatrizCiudades.graficarNeato(CiudadSeleccionada)
                    Posiciones = actual.MatrizCiudades.ubicarEntrada()
                    Civiles = actual.MatrizCiudades.ubicarUnidadCivil()
                actual = actual.siguiente
            
            VentanaNuevaMision = Toplevel()
            VentanaNuevaMision.title("Nueva Mision")
            VentanaNuevaMision.geometry("1100x900")
            VentanaNuevaMision.config(bg = "SkyBlue1")
            
            #ImagenCiudad = PhotoImage(file="matriz_"+CiudadSeleccionada+".png")
            #ImagenCiudad = ImagenCiudad.subsample(2,2)
            ImagenCiudad = Image.open("matriz_"+CiudadSeleccionada+".png") #abrir imagen
            ResizeImagen = ImagenCiudad.resize((700,700), Image.ANTIALIAS)
            ImagenCiudad = ImageTk.PhotoImage(ResizeImagen)
            LabelImagen = Label(VentanaNuevaMision, image = ImagenCiudad,bg="SkyBlue1",borderwidth=0)
            LabelImagen.place(x=25,y=100,width=700,height=700) 
            
            listasRobots = ttk.Combobox(VentanaNuevaMision, font=("Arial", 12, "italic"), width=20, height=5,state="readonly")
            Nombre = Nombre.split(",")
            listasRobots.config(values=Nombre)                            
            listasRobots.current(0)
            listasRobots.place(x=750,y=150)
            
            Label(VentanaNuevaMision, text = "Elegir Robot", font=("Arial", 12, "italic"),  bg="SkyBlue1").place(x=750,y=100,width=100)

            Entradas = ttk.Combobox(VentanaNuevaMision, font=("Arial", 12, "italic"), width=20, height=5,state="readonly")
            Posiciones = Posiciones.split(";")
            Entradas.config(values=Posiciones)                            
            Entradas.current(0)
            Entradas.place(x=750,y=400)
            Label(VentanaNuevaMision, text = "Elegir Punto de Entrada", font=("Arial", 12, "italic"),  bg="SkyBlue1").place(x=750,y=350,width=300)


            ListasCiviles = ttk.Combobox(VentanaNuevaMision, font=("Arial", 12, "italic"), width=20, height=5,state="readonly")
            Civiles = Civiles.split(";")
            ListasCiviles.config(values=Civiles)                            
            ListasCiviles.current(0)
            ListasCiviles.place(x=750,y=650)

            Button(VentanaNuevaMision, text="Realizar Misión", width=30, height=1, font=("Arial", 12, "italic"), command=self.MisionCompletada).place(x=450,y=850)
            Label(VentanaNuevaMision, text = "Elegir Unidad Civil", font=("Arial", 12, "italic"),  bg="SkyBlue1").place(x=750,y=600,width=300)
            Label(VentanaNuevaMision, text = "Menú Misiones", font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=200,y=25,width=600)
            VentanaNuevaMision.mainloop()
        

    def MisionExtraccion(self):
        global listarobotsCiudades
        global VentanaNuevaMision
        global  listasCiudades
        global VentanaElegirCiudad
        global VentanaNuevaMision
        global CiudadSeleccionada

        global listasRobots
        global ListasCiviles
        global Entradas

        Nombre = listarobotsCiudades.recorrerRecursos()
        ContadorUnidad = 0

        actual = self.cabeza
        while actual:
            ContadorUnidad = actual.ContadorUnidadMilitar
            actual = actual.siguiente
        ContadorChapinFighter=0
        
        print("Mision de Extracción")
        ContadorChapinFighter = listarobotsCiudades.ContadorChapinFighter

        if ContadorChapinFighter == 0:
            messagebox.showinfo("Error", "No hay robot ChapinFigther")
        elif ContadorUnidad == 0:  
            messagebox.showinfo("Error", "No hay Recursos")
        else:
            CiudadSeleccionada = listasCiudades.get()
            VentanaElegirCiudad.destroy()
            actual = self.cabeza
            while actual:
                if CiudadSeleccionada == actual.nombre:
                    print(actual.ContadorUnidadCivil)
                    actual.MatrizCiudades.graficarNeato(CiudadSeleccionada)
                    Posiciones = actual.MatrizCiudades.ubicarEntrada()
                    Civiles = actual.MatrizCiudades.ubicarRecursos()
                actual = actual.siguiente
            
            VentanaNuevaMision = Toplevel()
            VentanaNuevaMision.title("Nueva Mision")
            VentanaNuevaMision.geometry("1100x900")
            VentanaNuevaMision.config(bg = "SkyBlue1")
            
            #ImagenCiudad = PhotoImage(file="matriz_"+CiudadSeleccionada+".png")
            #ImagenCiudad = ImagenCiudad.subsample(2,2)
            ImagenCiudad = Image.open("matriz_"+CiudadSeleccionada+".png") #abrir imagen
            ResizeImagen = ImagenCiudad.resize((700,700), Image.ANTIALIAS)
            ImagenCiudad = ImageTk.PhotoImage(ResizeImagen)
            LabelImagen = Label(VentanaNuevaMision, image = ImagenCiudad,bg="SkyBlue1",borderwidth=0)
            LabelImagen.place(x=25,y=100,width=700,height=700) 
            
            listasRobots = ttk.Combobox(VentanaNuevaMision, font=("Arial", 12, "italic"), width=20, height=5,state="readonly")
            Nombre = Nombre.split(",")
            listasRobots.config(values=Nombre)                            
            listasRobots.current(0)
            listasRobots.place(x=750,y=150)
            
            Label(VentanaNuevaMision, text = "Elegir Robot", font=("Arial", 12, "italic"),  bg="SkyBlue1").place(x=750,y=100,width=100)

            Entradas = ttk.Combobox(VentanaNuevaMision, font=("Arial", 12, "italic"), width=20, height=5,state="readonly")
            Posiciones = Posiciones.split(";")
            Entradas.config(values=Posiciones)                            
            Entradas.current(0)
            Entradas.place(x=750,y=400)
            Label(VentanaNuevaMision, text = "Elegir Punto de Entrada", font=("Arial", 12, "italic"),  bg="SkyBlue1").place(x=750,y=350,width=300)

            ListasCiviles = ttk.Combobox(VentanaNuevaMision, font=("Arial", 12, "italic"), width=20, height=5,state="readonly")
            Civiles = Civiles.split(";")
            ListasCiviles.config(values=Civiles)                            
            ListasCiviles.current(0)
            ListasCiviles.place(x=750,y=650)
            Label(VentanaNuevaMision, text = "Elegir Unidad Civil", font=("Arial", 12, "italic"),  bg="SkyBlue1").place(x=750,y=600,width=300)
            
            Button(VentanaNuevaMision, text="Realizar Misión", width=30, height=1, font=("Arial", 12, "italic"), command = self.MisionCompletada).place(x=450,y=850)

            Label(VentanaNuevaMision, text = "Menú Misiones", font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=200,y=25,width=600)
            
            VentanaNuevaMision.mainloop()

    

        Label(VentanaNuevaMision, text = "Menú Misiones", font=("Arial", 16, "italic"),  bg="SkyBlue1").place(x=200,y=25,width=600)
        VentanaNuevaMision.mainloop()
    
    def elegirciudad (self, listarobots, ContadorCarga):
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
        
        Button(VentanaElegirCiudad, text="Misión de Rescate", width=30, height=1, font=("Arial", 12, "italic"), command=self.MisionRescate).grid(pady=5,padx=5, row=2, column=0)
        Button(VentanaElegirCiudad, text="Misión de Extracción de Recursos", width=30, height=1, font=("Arial", 12, "italic"), command=self.MisionExtraccion).grid(pady=5,padx=5, row=3, column=0)
        listasCiudades = ttk.Combobox(VentanaElegirCiudad, font=("Arial", 12, "italic"), width=20, height=5,state="readonly")
        ciudad = ''
        
        while actual: #"Ciudad1","Ciudad2","Ciudad3"
            if (ultimo.nombre==actual.nombre) and (ContadorCarga == 1):
                ciudad +=actual.nombre
            elif (ultimo.nombre==actual.nombre):
                ciudad += actual.nombre+','
            else:
                ciudad +=actual.nombre+','
            actual = actual.siguiente
        
        print(ciudad)
        ciudad = ciudad.split(",")
        listasCiudades.config(values=ciudad) 
        
                                          
        listasCiudades.current(0)
        listasCiudades.grid(pady=5,padx=5, row=1, column=0)
        VentanaElegirCiudad.mainloop()

    