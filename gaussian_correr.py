#!/bin/python3
import os 
import sys 
from io import open

class RunGaussian:

    def __init__(self,gaussian,ruta,extension):
        self.gaussian = gaussian
        self.ruta = ruta
        self.extension = extension


    def ruta_absoluta(self):
        """ entra a la ruta y extrae la absoluta"""
        os.chdir(self.ruta)
        y = os.getcwd()
        return y
        

    def leer_gaussian(self):

        """saca los archivos mol2"""
        ruta_absoluta = self.ruta_absoluta()
        archivos_ejecutables = []
        for archivo in os.listdir(ruta_absoluta):
            archivo_e = archivo.split(".")
            if archivo_e[1] == self.extension:
                archivos_ejecutables.append(f"{ruta_absoluta}/{archivo}")
        return archivos_ejecutables


    def correr_gaussian(self):
        """realiza el calculo"""
        archivos_ejecutables = self.leer_gaussian()

        try:
            for n in archivos_ejecutables:
                print('Corriendo {} {}'.format(self.gaussian,n.split("/")[-1]))
                os.system(f'{self.gaussian} {n}')
                print(f"finalizo {n}")
        except:
            print("error en el archivo")

    
        




carpeta = sys.argv[1]
Prueba = RunGaussian("g16", carpeta,"gjf")
Prueba.correr_gaussian()

