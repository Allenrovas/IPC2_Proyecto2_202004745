from tkinter import *
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from ListaCiudades import ListaCiudades, Ciudad
from tkinter import ttk
from tkinter import messagebox
from ListaUnidades import ListaUnidades, UnidadMilitar
from ListaRobots import ListaRobots, Robots

listaciudades = ListaCiudades()
listarobots = ListaRobots()
CargarArchivo = False
global VentanaPrincipal

def LeerXml():
    global CargarArchivo
    archivoinput = askopenfilename(filetypes=[("Archivos XML", ".xml"), ("All Files", ".*")])
    xmlentrada = ET.parse(archivoinput)
    raizxml = xmlentrada.getroot()
    
    for hijo in raizxml:
        
        if hijo.tag == 'listaCiudades':
            for subhijo in hijo:
                
                for subhijo2 in subhijo:
                    if subhijo2.tag == 'nombre':
                        filas = subhijo2.attrib['filas']
                        columnas = subhijo2.attrib['columnas']
                        nombre = subhijo2.text
                        nodo = Ciudad(nombre, filas, columnas)
                    elif subhijo2.tag == 'fila':
                        NumeroFila = subhijo2.attrib['numero']
                        Cadena = subhijo2.text
                        Cadena = Cadena.replace('"', '')
                        
                        ContadorColumns = 1
                        C = 0
                        for i in Cadena:
                            if Cadena[C] == '*':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "Intransitable")
                                    
                            elif Cadena[C] == ' ':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "Transitable")
                                    
                            elif Cadena[C] == 'E':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "Entrada")
                                    
                            elif Cadena[C] == 'C':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "unidadCivil")
                                    
                            elif Cadena[C] == 'R':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "Recurso")   
                              
                        

                    elif subhijo2.tag == 'unidadMilitar':
                        fila = subhijo2.attrib['fila']
                        fila = int(fila)
                        columna = subhijo2.attrib['columna']
                        columna = int(columna)
                        Combate = subhijo2.text
                        Combate = int(Combate)
                        nodo.MatrizCiudades.insertar(fila, columna, "unidadMilitar") 
                        nodo.ListaUnidades.insertar(fila, columna, Combate)

                print(nombre)
                listaciudades.insertar(nodo)
                
        elif hijo.tag == 'Robots':
            for subhijo in hijo:
                for subhijo2 in subhijo:
                    tipo = subhijo2.attrib['tipo']
                    try:
                        capacidad = subhijo2.attrib['capacidad']
                    except:
                        capacidad = None
                    nombre = subhijo2.text
                    nodo2 = Robots(tipo, capacidad, nombre)
                    listarobots.insertar(nodo2)
    CargarArchivo = True
    print("Se ha cargado el XML")

def MisionRescate():
    print("Mision de Rescate")

def MisionExtraccion():
    print("Mision de Extracción de Recursos")


def NuevaMision():
    global VentanaPrincipal
    global CargarArchivo
    if CargarArchivo == True:
        VentanaPrincipal.destroy()
        VentanaNuevaMision = Tk()
        VentanaNuevaMision.title("Nueva Mision")
        VentanaNuevaMision.geometry("300x300")
        VentanaNuevaMision.config(bg = "SkyBlue1")
        
        Label(VentanaNuevaMision, text = "Menú Misiones", font=("Arial", 16, "italic"),  bg="SkyBlue1").grid(pady=50, row=0, column=0)
        Button(VentanaNuevaMision, text="Misión de Rescate", width=30, height=1, font=("Arial", 12, "italic"), command=MisionRescate).grid(pady=5,padx=5, row=1, column=0)
        Button(VentanaNuevaMision, text="Misión de Extracción de Recursos", width=30, height=1, font=("Arial", 12, "italic"), command=MisionExtraccion).grid(pady=5,padx=5, row=2, column=0)
        VentanaNuevaMision.mainloop()
    else:
        VentanaPrincipal.destroy()
        messagebox.showinfo("Error", "No se ha cargado el archivo XML")
        Menu()
        

def Menu():
    global VentanaPrincipal
    VentanaPrincipal = Tk()
    VentanaPrincipal.title("Chapín Warriors, S. A.")
    VentanaPrincipal.config(bg="SkyBlue1")
    VentanaPrincipal.geometry("300x300")

    Label(VentanaPrincipal, text = "Chapín Warriors, S. A.", font=("Arial", 16, "italic"),  bg="SkyBlue1").grid(pady=50, row=0, column=0)
    Button(VentanaPrincipal, text="Cargar Archivo", width=30, height=1, font=("Arial", 12, "italic"), command=LeerXml).grid(pady=5,padx=5, row=1, column=0)
    Button(VentanaPrincipal, text="Nueva Misión", width=30, height=1, font=("Arial", 12, "italic"), command=NuevaMision).grid(pady=5,padx=5, row=2, column=0)


    VentanaPrincipal.mainloop()

Menu()

