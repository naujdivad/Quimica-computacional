#!/bin/bash

carpeta=$1
carpeta_destino=$2

mkdir $carpeta_destino

echo "Copiando archivos  a ${carpeta_destino}..." 
cp -r $carpeta/*/*/*z $carpeta_destino

echo "Descomprimiendo archivos..."
gunzip $carpeta_destino/*z
