import sys
import os


class ComprobarDondeQuedo():

    def __init__(self,ruta,extension):
        self.ruta = ruta
        self.extension=extension

    def sacar_ruta_absoluta(self):
        os.chdir(self.ruta)
        y = os.getcwd()
        return y
    
    def archivos_a_mirar(self):
        ruta_absoluta=self.sacar_ruta_absoluta()
        archivos_log= []
        for archivo in os.listdir(ruta_absoluta):
            archivo_e = archivo.split(".")
            if archivo_e[1] == self.extension:
                archivos_log.append(f"{ruta_absoluta}/{archivo}")
        return archivos_log

    def mirar_si_termino_bien(self):
        archivos_ejecutables=self.archivos_a_mirar()
        for log in archivos_ejecutables:
            archivo_log=open(log,"r")
            archivo_leido = archivo_log.readlines()
            ultima_linea = archivo_leido[-1].split(" ")
            
            if ultima_linea[1] == "Normal" and ultima_linea[2] == "termination":
                print(f'el archivo {log.split("/")[-1]} ha terminado bien')
            else:
                print(f'el archivo {log.split("/")[-1]} no termino bien')
        archivo_log.close()

carpeta = sys.argv[1]   
probemos = ComprobarDondeQuedo(carpeta,"log")
probemos.mirar_si_termino_bien()

    
        
