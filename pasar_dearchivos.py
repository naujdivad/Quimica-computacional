import os
import sys

class CambiaFormatos():
    def __init__(self,ruta,extension,extension_salida):
        self.ruta = ruta
        self.extension= extension
        self.extension_salida=extension_salida
        

    def ruta_absoluta(self):
        os.chdir(self.ruta)
        y = os.getcwd()
        return y
    
    def leer_archivos(self):
        """saca los archivos"""
        ruta_absoluta = self.ruta_absoluta()
        
        archivos_ejecutables = []
        
        for archivo in os.listdir(ruta_absoluta):
            archivo_e = archivo.split(".")
            if len(archivo_e)>1:
                if archivo_e[1] == self.extension:
                    archivos_ejecutables.append(f"{ruta_absoluta}/{archivo}")
        
        return archivos_ejecutables

    def pasemos(self):
        archivos_ejecutables = self.leer_archivos()
        
        try:
            for x in archivos_ejecutables:
                
                os.system(f'babel -i{self.extension} {x} -o{self.extension_salida} {x.split(".")[0]}.{self.extension_salida}')
        except:
            print(f"error en el archivo{x}")

extension =input("que formato de archivo quieres cambiar: ")
extension_salida = input("que formato de salida quieres: ")

carpeta = sys.argv[1]
probemos = CambiaFormatos(carpeta,extension,extension_salida)

probemos.pasemos()