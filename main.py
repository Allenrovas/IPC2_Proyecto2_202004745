from tkinter import *
import xml.etree.ElementTree as ET
from tkinter.filedialog import askopenfilename

def LeerXml():
    archivoinput = askopenfilename(filetypes=[("Archivos XML", ".xml"), ("All Files", ".*")])
    xmlentrada = ET.parse(archivoinput)
    raizxml = xmlentrada.getroot()
    for hijo in raizxml:
        if hijo == 'listaCiudades':
            print("hi")

LeerXml()
        