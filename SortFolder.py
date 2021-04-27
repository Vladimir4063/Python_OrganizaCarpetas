#Organiza carpetas segun su extension
#Organize folders according to their extension

#Import library - Importamos libreria

"""EJECUTAR VARIAS VECES."""

import os
import shutil 

#Ordenamos la carpeta "Descargas"

ruta_descargas = ("C:\\Users\\Vladimir_PC\\Downloads\\")

ruta_descargas = "C:\\Users\\Vladimir\\Descargas" 


ext_text = ['.docx', '.txt', '.doc', '.pdf', '.pptx']
ext_foto = ['.png', '.jpg', '.jpeg', '.gif']
ext_video = ['.mov', '.mp4']
ext_audio = ['.mp3']
ext_sfk = [".sfk"]

def ordenar(archivo, ext):
    for i in ext_text:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Textos') 

    for i in ext_foto:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Imagenes') 

    for i in ext_video:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Videos') 

    for i in ext_audio:
        if ext == i:
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Audio') 

    if ext != '':
            shutil.move(ruta_descargas + archivo, ruta_descargas + 'Otros') 

def main():
    for archivo in os.listdir(ruta_descargas):
        nombre_archivo, ext = os.path.splitext(archivo)
        ordenar(archivo, ext)

main()