from tkinter import *
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename
from ListaCiudades import ListaCiudades, Ciudad
from tkinter import ttk
from tkinter import messagebox
from ListaUnidades import ListaUnidades, UnidadMilitar
from ListaRobots import ListaRobots, Robots
from MatrizCiudades import MatrizCiudades

global listarobots

listaciudades = ListaCiudades()
listarobots = ListaRobots()
matrizciudades = MatrizCiudades()
CargarArchivo = False
global VentanaPrincipal



def LeerXml():
    global CargarArchivo
    global listarobots
    archivoinput = askopenfilename(filetypes=[("Archivos XML", ".xml"), ("All Files", ".*")])
    xmlentrada = ET.parse(archivoinput)
    raizxml = xmlentrada.getroot()
    
    for hijo in raizxml:
        
        if hijo.tag == 'listaCiudades':
            
            for subhijo in hijo:
                ContadorUnidadCivil = 0
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
                        
                        for i in Cadena:
                            if i== '*':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "Intransitable")
                                ContadorColumns += 1
                            elif i == ' ':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "Transitable")
                                ContadorColumns += 1  
                            elif i == 'E':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "Entrada")
                                ContadorColumns += 1
                            elif i == 'C':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "unidadCivil")
                                ContadorUnidadCivil += 1
                                ContadorColumns += 1
                                nodo.ContadorUnidadCivil = ContadorUnidadCivil
                            
                            elif i == 'R':
                                nodo.MatrizCiudades.insertar(int(NumeroFila), int(ContadorColumns), "Recurso")
                                ContadorColumns += 1 
                              
                        

                    elif subhijo2.tag == 'unidadMilitar':
                        fila = subhijo2.attrib['fila']
                        fila = int(fila)
                        columna = subhijo2.attrib['columna']
                        columna = int(columna)
                        Combate = subhijo2.text
                        Combate = int(Combate)
                        #print(fila, columna, "Unidad Militar")
                        nodo.MatrizCiudades.ubicarCoordenada(fila, columna,"unidadMilitar") #Ubica la coordena de Unidad Militar y la pone None
                        #nodo.MatrizCiudades.insertar(fila, columna, "unidadMilitar") 
                        nodo.ListaUnidades.insertar(fila, columna, Combate)

                listaciudades.insertar(nodo)
                
        elif hijo.tag == 'robots':
            for subhijo in hijo:
                for subhijo2 in subhijo:
                    tipo = subhijo2.attrib['tipo']
                    try:
                        capacidad = subhijo2.attrib['capacidad']
                    except:
                        capacidad = None
                    nombre = subhijo2.text
                    listarobots.insertar(nombre, tipo, capacidad)
    CargarArchivo = True
    print("Se ha cargado el XML")





def ElegirCiudad():
    global listarobots
    if CargarArchivo == True:
        
        listaciudades.elegirciudad(listarobots)
    else:
        messagebox.showinfo("Error", "No se ha cargado el archivo XML")
        


VentanaPrincipal = Tk()
VentanaPrincipal.title("Chapín Warriors, S. A.")
VentanaPrincipal.config(bg="SkyBlue1")
VentanaPrincipal.geometry("300x300")

Label(VentanaPrincipal, text = "Chapín Warriors, S. A.", font=("Arial", 16, "italic"),  bg="SkyBlue1").grid(pady=50, row=0, column=0)
Button(VentanaPrincipal, text="Cargar Archivo", width=30, height=1, font=("Arial", 12, "italic"), command=LeerXml).grid(pady=5,padx=5, row=1, column=0)
Button(VentanaPrincipal, text="Nueva Misión", width=30, height=1, font=("Arial", 12, "italic"), command=ElegirCiudad).grid(pady=5,padx=5, row=2, column=0)


VentanaPrincipal.mainloop()


