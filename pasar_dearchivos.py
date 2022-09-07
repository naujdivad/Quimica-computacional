import os
import sys

class CambiaFormatos():
    def __init__(self,ruta,extension,extensionsalida):
        self.ruta = ruta
        self.extension= extension
        self.extensionsalida=extensionsalida
        

    def ruta_absoluta(self):
        os.chdir(self.ruta)
        y = os.getcwd()
        return y
    
    def leer_archivos(self):
        """saca los archivos pdbqt"""
        ruta_absoluta = self.ruta_absoluta()
        
        archivos_ejecutables = []
        
        for archivo in os.listdir(ruta_absoluta):
            archivo_e = archivo.split(".")
            if archivo_e[1] == self.extension:
                archivos_ejecutables.append(f"{ruta_absoluta}/{archivo}")
        
        return archivos_ejecutables

    def pasemos(self):
        archivos_ejecutables = self.leer_archivos()
        
        try:
            for x in archivos_ejecutables:
                os.system(f'babel -i{self.extension} {x} -opdb {x.split(".")[0]}.{self.extensionsalida}')
            
        except:
            print(f"error en el archivo{x}")

extension=input("Que extension vas a cambiar? ")
extensionsalida=input("Que extension de salida quieres? ")

carpeta = sys.argv[1]
probemos = CambiaFormatos(carpeta,extension,extensionsalida)
probemos.pasemos()
