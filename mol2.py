import os 
import sys 

class CopiarTodo():
    def __init__(self,entrada, salida):
        self.entrada=entrada
        self.salida = salida
        
    
    def ruta_absoluta_entrada(self):
        """ entra a la ruta y extrae la absoluta"""
        os.chdir(self.entrada)
        y = os.getcwd()
        return y

    def losmol2(self):
        ruta_absoluta = self.ruta_absoluta_entrada()
        archivos_ejecutables = []
        for archivo in os.listdir(ruta_absoluta):
            archivo_e = archivo.split(".")
            if archivo_e[-1] == "mol2":
                archivos_ejecutables.append(f"{ruta_absoluta}/{archivo}")
        
        return archivos_ejecutables
       
                     
    def copiatodo(self):
        archivos_ejecutables=self.losmol2()
        salida=open(self.salida,"w")
        for mol in archivos_ejecutables:
            archivomol2=open(mol,"r")
            for linea in archivomol2:
                salida.write(linea)
        salida.close()
        return salida


carpeta = sys.argv[1]
salida = sys.argv[2]
pruebapave = CopiarTodo(carpeta, salida)
pruebapave.copiatodo()
