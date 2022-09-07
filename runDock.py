from os import system, listdir
from sys import argv
from multiprocessing import Pool, cpu_count, current_process

"""
······ Para instalar en otro pc ···············
Tener instalado python3 en el pc

    1) Crear una carpeta script en el pc
    2) Copiar el programa runDock.py en la carpeta script
    3) en el directorio del usuario editar el archivo .bashrc
    4) Escribir alias runDock="python3 ruta/scritp/runDock.py"
    5) cerrar .bashrc
    6) escribir . .bashrc
"""

folder = argv[1]
outputs = argv[2]

archivos = listdir(folder)
dpf = []

for archivo in archivos:
    archivo_dpf = archivo.split('.')
    if len(archivo_dpf) == 2 and archivo_dpf[1] == 'dpf':
        dpf.append(archivo)

def calcular_dock(archivo):
    print('Corriendo =>', archivo, '...')
    system(f'autodock4  -p ./{archivo}.dpf -l {outputs}/{archivo}.dlg')
    print(f'Docking para {archivo} termino...')


dlg_files = []
for archivo in dpf:
    archivo = archivo.split('.')[0]
    dlg_files.append(archivo)

if __name__ == '__main__':
    n = cpu_count() - 1
    print('Tendras', n, 'procesos en simultaneo')
    print('Corriendo dockings...')
    with Pool(n) as p:
        p.map(calcular_dock, dlg_files)
